from django.shortcuts import render
from django.http import JsonResponse
import io
import chardet # Import chardet for encoding detection
import os
from django.conf import settings

import sys
ezdxf_path = '/Users/user/Desktop/Repos/Quant/Env/lib/python3.10/site-packages'
sys.path.append(ezdxf_path)
import ezdxf

from .modules import *

def process_dxf_file(request):
    if request.method == 'POST' and request.FILES.get('dxf_file'):
        dxf_file = request.FILES['dxf_file']
        
        # Define the path where you want to save the file
        save_path = os.path.join(settings.BASE_DIR, '/Users/user/Desktop/Repos/Quant/Quant/bloq_app/static/dxf_files', dxf_file.name)
        
        # Save the uploaded file to the specified path
        with open(save_path, 'wb') as destination:
            for chunk in dxf_file.chunks():
                destination.write(chunk)
        
        # Process the DXF file
        # count = entity_count(save_path)
        # layers = get_layers(save_path)
                
        walls = walls_output(save_path, "A-WALL", 250)

        context = {'walls': walls}

        return render(request, 'show.html', context)

    return render(request, 'upload_dxf.html')

def entity_count(file_path):
    count = 0
    # Read the DXF file
    doc = ezdxf.readfile(file_path)
    modelspace = doc.modelspace()
    for entity in modelspace:
        if entity.dxftype() == 'LINE' and entity.dxf.layer == "A-WALL":
            count += 1
    return count

def get_layers(file_path):
    layers = []
    # Read the DXF file
    doc = ezdxf.readfile(file_path)
    for layer in doc.layers:
        layers.append(layer.dxf.name)
    return layers