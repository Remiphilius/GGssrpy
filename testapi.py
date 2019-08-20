import google_streetview.api

params = [{
	'size': '600x300', # max 640x640 pixels
	'location': '46.414382,10.013988',
	'heading': '151.78',
	'pitch': '-0.76',
	'key': 'NbQA-R94JYlq_lY2y6bmaM9Zj_A='
}]

# Create a results object
results = google_streetview.api.results(params)

help(google_streetview.api.urlencode)