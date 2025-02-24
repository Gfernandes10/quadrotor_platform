import csv
from collections import defaultdict

# Função para ler o arquivo CSV
def read_csv(file_path):
    tasks = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row)
    return tasks

# Função para organizar as tarefas por plataforma e componente
def organize_tasks(tasks):
    organized_tasks = defaultdict(lambda: defaultdict(list))
    for task in tasks:
        tags = task['tags'].strip('[]').split(', ')
        platform = next((tag for tag in tags if tag in ['mil', 'sil', 'hil']), None)
        component = next((tag for tag in tags if tag not in ['mil', 'sil', 'hil']), None)
        if platform and component:
            organized_tasks[platform][component].append(task)
    return organized_tasks

# Função para gerar o conteúdo do README.md
def generate_readme(organized_tasks):
    readme_content = "# Quadrotor Platform Project\n\n"
    readme_content += "## General Overview\n\n"
    
    # Função para definir a cor do status
    def get_status_color(status):
        if status.lower() == "open":
            return "gray"
        elif status.lower() in ["planned", "in progress"]:
            return "blue"
        elif status.lower() == "done":
            return "green"
        else:
            return "black"
    
    # General Overview
    for platform, components in organized_tasks.items():
        readme_content += f"### {platform.upper()} ({'Model-in-the-loop' if platform == 'mil' else 'Software-in-the-loop' if platform == 'sil' else 'Hardware-in-the-loop'})\n"
        for component, tasks in components.items():
            readme_content += f"#### {component.capitalize()}\n"
            for task in tasks:
                task_name = task['Task Name']
                task_status = task['Status']
                task_id = task['Task ID']
                # Adiciona cor ao status
                status_color = get_status_color(task_status)
                readme_content += f"- [{task_name}](#{task_id}) - <span style='color:{status_color};'>{task_status}</span>\n"
        readme_content += "\n"
    
    # Summary
    readme_content += "## Summary\n\n"
    for platform, components in organized_tasks.items():
        readme_content += f"### {platform.upper()}\n"
        for component, tasks in components.items():
            readme_content += f"#### {component.capitalize()}\n"
            for task in tasks:
                task_name = task['Task Name']
                task_id = task['Task ID']
                time_logged = task['Time Logged']
                task_content = task['Task Content']
                # Seção da task no Summary com o ID como âncora
                readme_content += f"<a id='{task_id}'></a>\n"
                readme_content += f"##### {task_name}\n"
                # Cabeçalho com informações da task
                readme_content += f"<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>\n"
                readme_content += f"<strong>Platform:</strong> {platform.upper()} | "
                readme_content += f"<strong>Component:</strong> {component.capitalize()} | "
                readme_content += f"<strong>Time spent:</strong> {time_logged}\n"
                readme_content += "</div>\n"
                # Descrição da task
                readme_content += f"**Description:**\n{task_content}\n\n"
    
    return readme_content

# Função principal
def main():
    csv_file_path = "c:/Users/Gabriel Fernandes/Desktop/quadrotor_platform/utils/2025-02-24T18_32_53.846Z Sennandes Games - 2025 - Quadrotor Platform.csv"
    tasks = read_csv(csv_file_path)
    organized_tasks = organize_tasks(tasks)
    readme_content = generate_readme(organized_tasks)
    
    with open('README.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    main()