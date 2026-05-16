#!/usr/bin/env python3
"""
Manifest generation script.

This script executes the 'tree' command on a directory to understand its structure
and generates a JSON manifest file.

Supported formats:
1. 'legacy': (default) Nested structure with 'metadata' and 'modules' keys.
2. 'git': Flat-ish nested structure matching 'git ls-tree' style used by modern VHL backend.

Usage:
    python scripts/generate_manifest.py <directory_path> [--format git|legacy] [-z]
"""

import os
import json
import subprocess
import hashlib
import logging
import argparse
import sys
import zipfile
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_checksum(file_path: Path, algo="sha256") -> str:
    """Calculate checksum of a file."""
    if algo == "sha256":
        hasher = hashlib.sha256()
    else:
        hasher = hashlib.sha1()
        
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hasher.update(byte_block)
        return f"{algo}:{hasher.hexdigest()}"
    except Exception as e:
        logger.warning(f"Could not calculate checksum for {file_path}: {e}")
        return f"{algo}:unknown"

def get_file_type(file_path: Path) -> str:
    """Determine file type based on extension."""
    ext = file_path.suffix.lower()
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.tiff'}
    if ext in image_extensions:
        return "image"
    return "plain-text"

def generate_git_style_manifest(target_path: Path) -> Dict[str, Any]:
    """Generates a manifest matching GitClientWrapper.get_tree_view()"""
    manifest = {}
    
    for root, dirs, files in os.walk(target_path):
        # Ignore .git and other common folders
        if '.git' in dirs:
            dirs.remove('.git')
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
            
        rel_root = os.path.relpath(root, target_path)
        if rel_root == ".":
            current_level = manifest
        else:
            parts = rel_root.split(os.sep)
            current_level = manifest
            for part in parts:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]
        
        for file in files:
            file_path = Path(root) / file
            current_level[file] = {
                "name": file,
                "rel_path": str(Path(rel_root) / file) if rel_root != "." else file,
                "type": "file",
                "checksum": get_checksum(file_path, algo="sha1")
            }
            
    return manifest

def generate_legacy_manifest(target_path: Path, ignore_list: List[str] = None) -> Optional[Dict[str, Any]]:
    """Legacy manifest generator using 'tree'."""
    try:
        cmd = ['tree', '-J', '--noreport']
        if ignore_list:
            ignore_pattern = "|".join(ignore_list)
            cmd.extend(['-I', ignore_pattern])
        cmd.append(str(target_path))
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        tree_data = json.loads(result.stdout)
    except Exception as e:
        logger.error(f"Failed to execute tree: {e}")
        return None

    root_contents = tree_data[0].get('contents', [])
    manifest = {
        "metadata": {
            "project_name": target_path.name,
            "manifest_version": "1.1.0",
            "total_files": 0,
            "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "format": "zip-contained"
        },
        "modules": {"root": {}}
    }

    # ... (rest of legacy logic omitted for brevity, but I'll keep it simple for now)
    # Actually, I'll just implement a simplified version of legacy logic too
    for item in root_contents:
        name = item.get('name')
        if item.get('type') == 'file':
            manifest["modules"]["root"][Path(name).stem] = {
                "name": name,
                "rel_path": ".",
                "type": "file",
                "checksum": get_checksum(target_path / name)
            }
        elif item.get('type') == 'directory':
            manifest["modules"][name] = {}
            # Simplified recursion
            for root, _, files in os.walk(target_path / name):
                rel_dir = os.path.relpath(root, target_path)
                for f in files:
                    manifest["modules"][name][Path(f).stem] = {
                        "name": f,
                        "rel_path": rel_dir,
                        "type": "file",
                        "checksum": get_checksum(Path(root) / f)
                    }
    
    return manifest

def create_project_zip(source_dir: Path, output_zip: str, manifest_path: Path):
    """Flatten project files and manifest into a single directory and zip it."""
    logger.info(f"Creating flattened zip archive: {output_zip}")
    project_name = source_dir.name
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        flat_project_dir = tmp_path / project_name
        flat_project_dir.mkdir()
        
        shutil.copy2(manifest_path, flat_project_dir / manifest_path.name)
        
        for root, _, files in os.walk(source_dir):
            if '.git' in root: continue
            for file in files:
                shutil.copy2(Path(root) / file, flat_project_dir / file)
        
        shutil.make_archive(output_zip.replace('.zip', ''), 'zip', root_dir=tmp_path, base_dir=project_name)
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--format", choices=['git', 'legacy'], default='git')
    parser.add_argument("-z", "--zip", action="store_true")
    args = parser.parse_args()
    
    target_path = Path(args.directory).resolve()
    manifest_filename = f"{target_path.name}_manifest.json"
    
    if args.format == 'git':
        data = generate_git_style_manifest(target_path)
    else:
        data = generate_legacy_manifest(target_path)
        
    with open(manifest_filename, 'w') as f:
        json.dump(data, f, indent=2)
    logger.info(f"Generated {args.format} manifest: {manifest_filename}")
    
    if args.zip:
        create_project_zip(target_path, f"{target_path.name}.zip", Path(manifest_filename))

if __name__ == "__main__":
    main()
