import os
import shutil
import subprocess

TEMPLATE_DIR = "templates"

def assemble_project(component_code_map: dict, all_dependencies: set, output_dir: str):
    """
    Constructs the complete Next.js application by combining components, layout structure, and required packages.
    This function strategically organizes the page.tsx file.
    """
    print(f"🎬 [Builder] Initiating application assembly workflow at path: '{output_dir}'...")

    # Step 1: Remove existing directory
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Step 2: Duplicate base template
    try:
        print(f"   -> [Template] Replicating foundation template from '{TEMPLATE_DIR}'...")
        ignore_patterns = shutil.ignore_patterns('node_modules', '.next', 'package-lock.json', 'pnpm-lock.yaml')
        shutil.copytree(TEMPLATE_DIR, output_dir, ignore=ignore_patterns)
    except Exception as e:
        print(f"❌ [ERROR] Template directory replication unsuccessful: {e}")
        return

    # Step 3: Establish components folder
    components_dir = os.path.join(output_dir, "app", "components")
    os.makedirs(components_dir, exist_ok=True)

    # Step 4: Output individual component modules
    print("   -> [Components] Persisting generated component modules to filesystem...")
    for component_name, code in component_code_map.items():
        file_path = os.path.join(components_dir, f"{component_name}.tsx")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"      + Exported: app/components/{component_name}.tsx")
        except Exception as e:
            print(f"❌ [ERROR] Component module '{component_name}' write operation failed: {e}")

    # Step 5: ADAPTIVE LAYOUT COMPOSITION ENGINE
    print("   -> [Layout] Constructing adaptive page structure in app/page.tsx...")

    # Categorize components by position
    sidebar_comp = None
    header_comp = None
    other_comps = []

    component_names = list(component_code_map.keys())

    for name in component_names:
        if "sidebar" in name.lower():
            sidebar_comp = name
        elif "header" in name.lower() and "project" not in name.lower():
            header_comp = name
        else:
            other_comps.append(name)

    # Construct import declarations
    imports = ""
    for name in component_names:
        imports += f"import {name} from './components/{name}';\n"

    # Assemble JSX structure with predefined arrangement pattern
    jsx = f"""
'use client';

import React from 'react';
{imports}

export default function Home() {{
  return (
    <main className="flex h-screen bg-white text-gray-900">
      {f'<aside className="w-64 h-full flex-shrink-0 bg-[#25282F]"><{sidebar_comp} /></aside>' if sidebar_comp else ''}

      <div className="flex-1 flex flex-col h-full overflow-auto">
        {f'<header className="sticky top-0 z-10"><{header_comp} /></header>' if header_comp else ''}

        <div className="flex-1 flex flex-col">
          {''.join([f"<{comp} />" for comp in other_comps])}
        </div>
      </div>
    </main>
  );
}}
"""

    # Persist primary page module
    target_page_path = os.path.join(output_dir, "app", "page.tsx")
    try:
        with open(target_page_path, "w", encoding="utf-8") as f:
            f.write(jsx)
        print("   -> [Layout] Main page structure 'app/page.tsx' assembled with optimized component arrangement.")
    except Exception as e:
        print(f"❌ [ERROR] Primary page layout write operation unsuccessful: {e}")
        return

    # Step 6: Set up package dependencies
    print("   -> [Dependencies] Initiating package installation through pnpm (may require some time)...")
    try:
        install_command = ["pnpm", "install"]

        if all_dependencies:
            install_command.extend(list(all_dependencies))
            print(f"   -> [Dependencies] Setting up core packages plus AI-specified libraries: {list(all_dependencies)}")
        else:
            print("   -> [Dependencies] Setting up core packages exclusively...")

        subprocess.run(
            install_command,
            cwd=output_dir,
            check=True,
            capture_output=True  # Suppress installation logs
        )
        print("   -> [Dependencies] Package installation finalized successfully.")

    except subprocess.CalledProcessError as e:
        if e.errno == 2:
            print("❌ [ERROR] 'pnpm' command-line tool unavailable in system PATH.")
            print("   -> Required Action: Execute 'npm install -g pnpm' for installation.")
        else:
            print(f"❌ [ERROR] Package installation encountered errors. Log:\n{e.stderr.decode()}")
        return

    print("✅ [Builder] Application assembly workflow finalized successfully.")