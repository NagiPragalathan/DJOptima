# DJOptima ToolKit for Django

The **DJOptima ToolKit for Django** is an all-in-one utility designed to simplify and enhance the deployment process of Django projects, particularly tailored for seamless integration with the Vercel hosting platform. This toolkit empowers developers with a range of powerful features, streamlining essential tasks and boosting productivity.

## Features

- **HTML to Django Conversion**: Transform your existing HTML files into Django template format effortlessly. This feature accelerates the migration process, ensuring a smooth transition to Django's templating system.
    
- **Custom Template Tags**: Create and manage custom template tags effortlessly, allowing you to extend the capabilities of your Django templates. Empower your templates with dynamic functionality and flexibility.
    
- **Base Model Templates**: Seamlessly manage base model templates, encompassing essential aspects such as handling static files and modifying settings content. Maintain consistency and coherence across your project's design effortlessly.
    
- **Vercel Hosting Support**: Automate the generation of vital deployment files, including `vercel.json`, `build_files.sh`, and `requirements.txt`. Simplify the setup process for hosting your Django project on the Vercel platform.
    

## Modules and Functions

- **Base.py**: Provides functions for creating necessary project folders and updating base settings. This module lays the groundwork for your Django project's configuration.
    
- **Host.py**: Facilitates the creation of essential files and configurations required for Vercel hosting. This module streamlines the deployment process and ensures optimal compatibility with the Vercel platform.
    
- **Template.py**: Offers a set of tools to seamlessly convert HTML files into Django template format. Enhance your project's efficiency by seamlessly integrating your existing HTML content.
    
- **Designer**: Incorporates modules that enable easy customization of foreground and background colors. Tailor your console output to your preferences for a more enjoyable coding experience.
    
- **vercelkit.py**: A specialized toolkit catered specifically for deploying Django projects on the Vercel platform. This module optimizes the deployment process and minimizes configuration overhead.

# vercelkit.py - Streamlined Deployment of Django Projects to Vercel

The `vercelkit.py` module offers a toolkit for simplifying the deployment of Django projects to the Vercel platform. It includes functions for generating deployment files, configuring settings, and automating the deployment process.

## Usage

Import and utilize the functions within this module to streamline the deployment of your Django project to Vercel. Refer to the individual function documentation for detailed information on usage and parameters.

## Features

- `generate_vercel_files()`: Generate deployment files required for Vercel deployment.
- `configure_project_settings()`: Configure project settings for Vercel deployment.
- `automate_deployment()`: Automate the deployment process to Vercel.

## Functions

- `generate_vercel_files()`: Generate Vercel-specific deployment files.
- `configure_project_settings()`: Configure project settings for Vercel deployment.
- `automate_deployment()`: Automate the deployment process to Vercel.

## Function Details

### 1. `print_version()`

This function prints the version information of the script.

**Usage:**
```python
print_version()
```

### 2. `print_help()`

This function prints a help message explaining the available commands and options.

**Usage:**
```python
print_help()
```

### 3. `print_error(message)`

This function prints an error message in red.

**Usage:**
```python
print_error(message)
```

### Command-line Arguments and Options

- `--base`: Creates the base folders required for a new Django project.
- `--vercelhost`: Generates files and updates settings for deploying on Vercel hosting.
- `--inphtml <path>`: Converts an HTML file to a Django template format.
- `--djhtml`: Generates a Django HTML template file.
- `--version` / `--V` / `--v`: Displays the version of the script.
- `-h`, `--help`: Displays the help message.

## Flow

1. **Version and Help Information**
   - The `print_version()` function displays the version of the script.
   - The `print_help()` function provides information on available commands and options.

2. **Error Handling**
   - The `print_error(message)` function displays an error message in red.

3. **Command-line Argument Handling**
   - The script checks for various command-line arguments and performs corresponding actions:
     - `--base`: Creates base folders required for a new Django project.
     - `--vercelhost`: Generates files and updates settings for Vercel hosting.
     - `--inphtml <path>`: Converts an HTML file to a Django template format.
     - `--djhtml`: Generates a Django HTML template file.
     - `--version` / `--V` / `--v`: Displays the version of the script.
     - `-h`, `--help`: Displays the help message.

# Base.py - Essential Functions for Django Project Setup and Configuration

The **Base.py** module provides a collection of essential functions tailored to simplify Django project setup, configuration, and optimization. By offering tools for creating folders, managing settings, and enhancing configurations, this module streamlines the development process and ensures a solid foundation for your Django projects.

## Usage

Import and utilize the functions within this module to perform various tasks related to Django project setup and configuration.

## Features and Functions

### `create_folders()`

Creates the necessary 'templates' and 'static' folders for your Django project. If these folders don't already exist, this function creates them. It also modifies Django settings and URLs files to include the 'templates' folder in the 'DIRS' list.

#### Example:

```python
# Create necessary folders and modify settings
create_folders()
```

### `add_to_installed_apps(file_path, app_name)`

Adds an app to the INSTALLED_APPS list in your project's settings file.

#### Example:

```python
# Add 'myapp' to INSTALLED_APPS in settings.py
add_to_installed_apps('path/to/settings.py', 'myapp')
```

### `set_allowed_hosts(file_path, desired_allowed_hosts)`

Sets the desired ALLOWED_HOSTS list in your project's settings file.

#### Example:

```python
# Set ALLOWED_HOSTS to a list of desired hosts
set_allowed_hosts('path/to/settings.py', "['localhost', 'example.com']")
```

### `comment_out_databases(file_path)`

Comments out the DATABASES configuration in your project's settings file.

#### Example:

```python
# Comment out the DATABASES configuration
comment_out_databases('path/to/settings.py')
```

### `update_static_settings(file_path)`

Updates static and media settings in your project's settings file.

#### Example:

```python
# Update static and media settings
update_static_settings('path/to/settings.py')
```

### `base_edit_settings_file(settings_file_path)`

Performs a series of base configuration updates on your project's settings file, including adding the app to INSTALLED_APPS, setting ALLOWED_HOSTS, and updating static settings.

#### Example:

```python
# Perform base configuration updates
base_edit_settings_file('path/to/settings.py')
```

## Note

- This module assumes it's being run within a Django project directory.
- It relies on functions from other modules such as `t_size()`, `blue()`, `green()`, `get_app_name()`, `base_edit_settings_file()`, and `edit_urls_file()`.
- Make sure to customize the module according to your project's structure and requirements.

For detailed usage instructions and examples, refer to the comments within the codebase.

# Host.py - Streamline Hosting and Deployment in Django Projects

The `Host.py` module simplifies the hosting and deployment process for Django projects. It provides tools to generate necessary files, configure settings, and streamline the deployment of your project to hosting platforms like Vercel.

## Usage

This module is designed to be imported and used within your Django project to facilitate the hosting and deployment process.

## Features

- `generate_files()`: Generates essential files required for deployment, such as 'vercel.json', 'requirements.txt', and 'build_files.sh'.
- `Change_the_files()`: Performs a series of essential configuration updates for deployment, including updating settings, WSGI files, and URLs.
- `Host.djangotemp()`: Batch convert HTML files to Django template format in the 'Host.py' module.

## Functions

- `generate_files()`: Generates essential deployment files.
- `Change_the_files()`: Performs essential configuration updates for deployment.
- `Host.djangotemp()`: Batch convert HTML files to Django template format.
- ... (Other functions related to hosting and deployment.)

## Function Details

### 1. `generate_files()`

This function generates specific files within the current directory for a Django project. It creates the following files: 'vercel.json', 'requirements.txt', 'build_files.sh', and 'README.md'.

**Usage:**
```python
generate_files()
```

**Example:**
```python
generate_files()
```

### 2. `Change_the_files()`

This function performs a series of file edits and updates for a Django project. It updates the 'settings.py', 'wsgi.py', and 'urls.py' files based on the project's configuration.

**Usage:**
```python
Change_the_files()
```

**Example:**
```python
Change_the_files()
```

### 3. `Host.djangotemp()`

This function is intended to batch convert HTML files to Django template format. It provides a utility to automate the conversion process.

**Usage:**
```python
Host.djangotemp()
```

**Example:**
```python
Host.djangotemp()
```

## Flow

1. **Finding Views Folder and Terminal Size**
   - The `find_views_folder()` function searches for the 'views' folder within the current Django project directory.
   - The `t_size()` function retrieves the size of the terminal window.

2. **Getting Imported Modules and Versions**
   - The `get_imported_modules(file_path)` function retrieves a set of imported modules from a given Python source file.
   - The `find_imported_modules(root_dir)` function finds and returns a list of imported modules across Python files within a directory.
   - The `get_modules_version(module_datas)` function retrieves version information for a list of modules.
   - The `shortcut_version(root_dir)` function quickly retrieves version information for imported modules within a directory.

3. **Getting App Name of Django**
   - The `get_app_name()` function retrieves the Django app name based on the current project's `manage.py` file.

4. **Creating the Needed Files for Deployment**
   - The `generate_files()` function generates 'vercel.json', 'requirements.txt', and 'build_files.sh' files within the current directory.

5. **Editing Files**
   - Various functions like `add_to_installed_apps()`, `set_allowed_hosts()`, `comment_out_databases()`, and `update_static_settings()` are used to edit the `settings.py` file.
   - The `edit_wsgi_file()` function edits the `wsgi.py` file to include "app = application" if not present.
   - The `edit_urls_file()` function adds content to the `urls.py` file for serving media and static files.

6. **Base Edit Settings File**
   - The `base_edit_settings_file(settings_file_path)` function performs various edits to the base settings file of a Django project.

7. **Edit Settings File**
   - The `edit_settings_file(settings_file_path)` function performs various edits to the settings file for Vercel hosting.

8. **Edit WSGI File**
   - The `edit_wsgi_file(wsgi_file_path)` function edits a WSGI file by updating it using the `update_wsgi_file` function.

9. **Edit URLs File**
   - The `edit_urls_file(file_path)` function edits a URLs file by updating it with additional content using the `update_urlpatterns` function.

10. **Executing Change_the_files()**
   - The `Change_the_files()` function coordinates the sequence of edits and updates required for deployment.

# Template.py - Advanced Terminal Styling for Django Templates

The `Template.py` module enhances terminal-based styling and provides tools to convert HTML content into Django template format. It introduces advanced terminal size retrieval for more precise styling and offers a function to seamlessly convert HTML files into Django template format with static tag replacements.

## Usage

This module is intended to be imported and used within your Django project for terminal-based styling enhancements and HTML-to-template conversion.

## Features

- `t_size()`: A function to retrieve advanced terminal dimensions for responsive styling.
- `convert_to_django_html(input_file, output_file)`: Converts HTML files to Django template format by replacing 'href' and 'src' attributes with Django static tags.
- `djangotemp()`: Converts HTML files in the current directory to Django template format, saving them in an 'output_html_files' directory.

## Functions

- `t_size()`: Retrieves advanced terminal dimensions for precise styling in templates.
- `convert_to_django_html(input_file, output_file)`: Converts HTML to Django template format with static tag replacements.
- `djangotemp()`: Batch converts HTML files to Django template format in the current directory.

## Function Details

### 1. `t_size()`

This function retrieves the current terminal size in columns (width) and lines (height). It uses the `os.get_terminal_size()` method to obtain the dimensions of the current terminal window.

**Usage:**
```python
t_size()
```

**Example:**
```python
terminal_dimensions = t_size()
print("Terminal Width:", terminal_dimensions[0])
print("Terminal Height:", terminal_dimensions[1])
```

### 2. `convert_to_django_html(input_file, output_file)`

This function converts an HTML file to Django template format by replacing 'href' and 'src' attributes with Django static tags. It ensures that the HTML content becomes compatible with Django templates.

**Usage:**
```python
convert_to_django_html(input_file, output_file)
```

**Example:**
```python
input_file_path = "input.html"
output_file_path = "output_template.html"
convert_to_django_html(input_file_path, output_file_path)
```

### 3. `djangotemp()`

This function batch converts HTML files in the current directory to Django template format. It replaces 'href' and 'src' attributes with Django static tags, and the converted files are saved in an 'output_html_files' directory.

**Usage:**
```python
djangotemp()
```

**Example:**
```python
djangotemp()
```

## Flow

1. **Advanced Terminal Styling**
   - The `t_size()` function retrieves terminal dimensions for responsive styling.

2. **HTML-to-Template Conversion**
   - The `convert_to_django_html(input_file, output_file)` function converts HTML to Django template format.
   - It replaces 'href' and 'src' attributes with Django static tags for compatibility.

3. **Batch Conversion with djangotemp()**
   - The `djangotemp()` function searches for HTML files in the current directory.
   - It converts them to Django template format and saves them in an 'output_html_files' directory.


how to use the `vercelkit.py` module along with usage examples:

```python
def print_help():
    """Prints the help message."""
    print("-")
    print("Django Project Helper Script")
    print("This script provides various utilities to assist in managing a Django project.")
    print("\nUsage:")
    print(f"  {blue('--base')}           {pink('Create base folders')} for a new Django project.")
    print(f"  {blue('--vercelhost')}     Generate files and {pink('update settings')} for {pink('Vercel hosting')}.")
    print(f"  {blue('--inphtml <path>')} Convert an HTML file to {pink('Django template')} format.")
    print(f"  {blue('--djhtml')}         Generate a {pink('Django HTML template')}.")
    print(f"  {blue('--version')}        Display {pink('version information')}.")
    print(f"  {blue('-h, --help')}       Display {pink('this help message')}.")
    print("\nOptions:")
    print(f"  {blue('--base')}:")
    print("    Creates the base folders required for a new Django project.")
    print(f"  {blue('--vercelhost')}:")
    print("    Generates files and updates settings for deploying on Vercel hosting.")
    print(f"  {blue('--inphtml <path>')}:")
    print("    Converts an HTML file to a Django template format.")
    print(f"  {blue('--djhtml')}:")
    print("    Generates a Django HTML template file.")
    print(f"  {blue('--version')} / {blue('--V')} / {blue('--v')}:")
    print("    Displays the version of the script.")
    print("\nColor Codes:")
    print(f"  {red('Red')}, {blue('Blue')}, {green('Green')}, {yellow('Yellow')}, {brown('Brown')}, {pink('Pink')}")

# Print the help message
print_help()
```

---

# `DJOptima` - Streamlined Deployment of Django Projects to Vercel

The `djoptima` module offers a toolkit for simplifying the deployment of Django projects to the Vercel platform. It includes functions for generating deployment files, configuring settings, and automating the deployment process.

## Usage

1. **Print Help Message:**
   Run the script without any arguments or with `-h`/`--help` to see the available commands and options.

   Example:
   ```bash
   djoptima -h
   ```

2. **Create Base Folders:**
   Use the `--base` argument to create the base folders required for a new Django project.

   Example:
   ```bash
   djoptima --base
   ```

3. **Generate Vercel Files and Update Settings:**
   Use the `--vercelhost` argument to generate files and update settings for deploying on Vercel hosting.

   Example:
   ```bash
   djoptima --vercelhost
   ```

4. **Convert HTML to Django Template Format:**
   Use the `--inphtml <path>` argument to convert an HTML file to a Django template format.

   Example:
   ```bash
   djoptima --inphtml input.html
   ```

5. **Generate Django HTML Template:**
   Use the `--djhtml` argument to generate a Django HTML template file.

   Example:
   ```bash
   djoptima --djhtml
   ```

6. **Display Version Information:**
   Use the `--version`, `--V`, or `--v` argument to display the version of the script.

   Example:
   ```bash
   djoptima --version
   ```

## Color Codes

- Red, Blue, Green, Yellow, Brown, Pink: Color codes for enhanced readability.

## Examples

- To create base folders for a new Django project:
  ```bash
  djoptima --base
  ```

- To generate Vercel deployment files and update settings:
  ```bash
  djoptima --vercelhost
  ```

- To convert an HTML file to a Django template format:
  ```bash
  djoptima --inphtml input.html
  ```

- To generate a Django HTML template file:
  ```bash
  djoptima --djhtml
  ```

- To display the version of the script:
  ```bash
  djoptima --version
  ```

For more information and details on the functionalities, use the `--help` option:

```bash
djoptima --help
```

---
