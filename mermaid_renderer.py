import subprocess
import os
import shutil

class MermaidRenderer:
    def __init__(self, width=3840, height=3840, scale=4, theme="default"):
        self.width = width
        self.height = height
        self.scale = scale
        self.theme = theme

        # Check once and store the paths
        self.node_path = shutil.which("node")
        self.mmdc_path = shutil.which("mmdc")

        if self.node_path is None or self.mmdc_path is None:
            missing = []
            if self.node_path is None:
                missing.append("node.js")
            if self.mmdc_path is None:
                missing.append("mmdc (mermaid-cli)")
            print(f"🔴 missing required tools: {', '.join(missing)}. please install them before proceeding.")

    def mermaid_snap(self, diagram_code, snap_name="diagram_4k.png"):
        # Use a single if block with 'or' to check prerequisites
        if self.node_path is None or self.mmdc_path is None:
            print("🔴 cannot generate diagram because required tools are missing.")
            return

        temp_file = "temp_diagram.mmd"
        try:
            with open(temp_file, "w") as f:
                f.write(diagram_code)

            subprocess.run(
                [
                    self.mmdc_path,
                    "-i", temp_file,
                    "-o", snap_name,
                    "-w", str(self.width),
                    "-H", str(self.height),
                    "-s", str(self.scale),
                    "-t", self.theme,
                ],
                capture_output=True,
                text=True,
                check=True,
            )

        except Exception as err:
            print(f"🔴 mermaid snap failed: {err}")
            if hasattr(err, 'stderr') and err.stderr:
                print(err.stderr)
            return

        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

        print(f"🟢 mermaid snap done: {snap_name} ({self.width}x{self.height}, scale={self.scale})")


# Example usage

# your mermaid diagram code as a string
mermaid_code = """
sequenceDiagram
    participant Alice
    participant Bob

    Alice->>Bob: Hello Bob, how are you?
    Bob-->>Alice: I am good, thanks!
    Alice->>Bob: Great to hear!

"""

# create an instance of MermaidRenderer
renderer = MermaidRenderer()

# generate a high-quality PNG image file named 'my_diagram.png'
renderer.mermaid_snap(mermaid_code, snap_name="my_diagram.png")
