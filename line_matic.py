def line_matic(src_file_path, dest_file_path, verbose=False):
    try : 
        with open(src_file_path, 'r') as file:
            lines = file.readlines()

        cnt_blank_lines = sum(1 for line in lines if not line.strip())
        non_empty_lines = [line for line in lines if line.strip()]

        hash_lines = []
        for i, line in enumerate(non_empty_lines):
            line_number = f"[ # {i+1:>15} ]        "  
            content = line.rstrip()  
            hash_lines.append(f"{line_number}{content}")
        
        if verbose:
            print(f"[ meta-info ] : number of empty lines removed: {cnt_blank_lines}")
        with open(dest_file_path, 'w') as file:
            file.write("\n".join(hash_lines))
        
        if verbose:
            print(f"[ meta-info ] : processed content saved to {dest_file_path}")
        return "\n".join(hash_lines)
    
    except Exception as e:
        print(f"[ meta-critical ] : unable to process file, an exception occured : {e}")
        return None
