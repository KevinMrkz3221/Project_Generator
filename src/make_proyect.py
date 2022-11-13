import os
import shutil
import templates

def create_three(fullpath):
    os.mkdir(fullpath+'/resources')
    os.mkdir(fullpath+'/app')
    os.mkdir(fullpath+'/src')
    os.mkdir(fullpath+'/include')
    os.mkdir(fullpath+'/data')
    os.mkdir(fullpath+'/Notebooks')
    os.mkdir(fullpath+'/docs')

def create_directories(path, name, selector=0):
    full_path = path + name
    try:
        if not selector:
            os.mkdir(full_path)
            create_three(full_path)
        else:
            os.rmdir(full_path)
            os.mkdir(full_path)
            create_three(full_path)
        return 1
    except FileExistsError: 
        return 0
    except OSError:
        shutil.rmtree(full_path) 
        os.mkdir(full_path)
        create_three(full_path)

def create_include_files(path, name):
    full_path = path + name

    with open(f'{full_path}/include/__init__.py', 'w') as file:
        file.write(templates.Include_init_template)
    file.close()

    with open(f'{full_path}/include/thread.py', 'w') as file:
        file.write(templates.thread_template)
    file.close()

def create_app_files(path, name, TApp):
    full_path = path + name

    with open(f'{full_path}/app/app.py', 'w') as file:
        file.write(TApp)
    file.close()

    with open(f'{full_path}/app/__init__.py', 'w') as file:
        file.write(templates.App_init_template)
    file.close()

def create_src_files(path, name, TRun):
    full_path = path + name

    with open(f'{full_path}/src/run.py', 'w') as file:
        file.write(TRun)
    file.close()

    with open(f'{full_path}/src/__init__.py', 'w') as file:
        file.write(templates.src_init_template)
    file.close()

def create_main_file(path, name):
    full_path = path + name

    with open(f'{full_path}/main.py', 'w') as file:
        file.write(templates.main_template)
    file.close()

def create_python_files(path, name, TApp, TRun):
    create_include_files(path, name)
    create_app_files(path, name, TApp)
    create_src_files(path, name, TRun)
    create_main_file(path, name)
    shutil.copy('./resources/favicon.ico', path+name+'/resources/favicon.ico')