from flask import Flask, render_template, redirect, url_for, request
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    containers = client.containers.list(all=True)
    return render_template('index.html', containers=containers)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        container_name = request.form.get('container_name').lower().replace(' ', '_')
        image_name = request.form.get('image_name')
        host_port = int(request.form.get('host_port'))
        container_port = int(request.form.get('container_port'))
        
        try:
            # Remove old container with same name
            try:
                old = client.containers.get(container_name)
                old.stop()
                old.remove()
            except:
                pass
            
            # Create new container
            client.containers.run(
                image=image_name,
                name=container_name,
                detach=True,
                ports={f'{container_port}/tcp': host_port}
            )
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {e}<br><a href='{url_for('index')}'>Back</a>", 500
    
    return render_template('create.html')

@app.route('/delete/<container_id>')
def delete(container_id):
    try:
        container = client.containers.get(container_id)
        container.stop()
        container.remove()
    except Exception as e:
        pass  # Already deleted
    return redirect(url_for('index'))

@app.route('/open/<container_id>')
def open_container(container_id):
    container_info = client.containers.get(container_id)
    # Get first available port mapping
    ports = container_info.attrs['NetworkSettings']['Ports']
    for port_key, port_list in ports.items():
        if port_list:
            actual_host_port = port_list[0]['HostPort']
            return redirect(f'http://localhost:{actual_host_port}/')
    return "No ports exposed", 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
