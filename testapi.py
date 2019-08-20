import google_streetview.api

params = [{
	'size': '600x300',  # max 640x640 pixels
	'location': '46.414382, 10.013988',
	'heading': '151.78',
	'pitch': '-0.76',
	'key': r'AIzaSyDP-PDpFh1qaZzUnl7qSbMr76AkkW7Gl_0'
}]

# Create a results object
results = google_streetview.api.results(params)

print(results.metadata)
