from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"apple", "limit":20, "print_urls":True}
response.download(arguments)