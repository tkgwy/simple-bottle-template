import sys
import os
import bottle

app = bottle.default_app()

@app.route('/')
def index():
	return 'Hello, world!'


def get_config_path(profile, filename='app.conf'):
	return os.path.join(os.path.dirname(__file__), 'config', profile, filename)

def load_options(config_file_path):
	app.config.load_config(config_file_path)

def main(config_file_path=None):
	profile = os.environ.get('PROFILE', 'development')
	if config_file_path is None:
		config_file_path = get_config_path(profile)
	load_options(config_file_path)
	app.run(host=app.config['web.host'], port=app.config['web.port'], debug=app.config['web.debug'], reloader=app.config['web.auto_reload'])

if __name__ == '__main__':
	args = sys.argv
	config_file_path = args[1] if len(args) > 1 else None
	main(config_file_path)
