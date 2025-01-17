import json
import ollama

def get_ollama_config():
    try:
        models = ollama.list().models
    except Exception as e:
        return json.dumps({"error": f"Failed to fetch models: {str(e)}"})

    model_list = []

    for model_name, modified_at, digest, size, details in models:
        model_name_value = model_name[1]
        family = details[1].family
        parameter_size = details[1].parameter_size
        model_size_gb = f"{round(size[1] / (1000 ** 3), 1)} GB"

        model_list.append({
            "model_name": model_name_value,
            "model_family": family,
            "model_parameter_size": parameter_size,
            "model_size": model_size_gb
        })

    return json.dumps(model_list, indent=4)

print(get_ollama_config())
