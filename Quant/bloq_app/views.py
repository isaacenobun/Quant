from django.shortcuts import render,redirect
import os
from django.conf import settings

# import sys
# ezdxf_path = '/Users/user/Desktop/Repos/Quant/Env/lib/python3.10/site-packages'
# sys.path.append(ezdxf_path)
# import ezdxf

from .modules import *
from .models import *

# def process_dxf_file(request):
#     if request.method == 'POST' and request.FILES.get('dxf_file'):
#         dxf_file = request.FILES['dxf_file']
        
#         # Define the path where you want to save the file
#         save_path = os.path.join(settings.BASE_DIR, '/Users/user/Desktop/Repos/Quant/Quant/bloq_app/static/dxf_files', dxf_file.name)
        
#         # Save the uploaded file to the specified path
#         with open(save_path, 'wb') as destination:
#             for chunk in dxf_file.chunks():
#                 destination.write(chunk)
        
#         # Process the DXF file
#         # count = entity_count(save_path)
#         # layers = get_layers(save_path)
                
#         walls = walls_output(save_path, "A-WALL", 250)

#         context = {'walls': walls}

#         return render(request, 'show.html', context)

#     return render(request, 'upload_dxf.html')

def home(request):
    if request.method == 'POST' and request.FILES.get('dxf_file'):
        dxf_file = request.FILES['dxf_file']
        save_path = os.path.join(settings.BASE_DIR, '/Users/user/Desktop/Repos/Quant/Quant/bloq_app/static/dxf_files', dxf_file.name)
        with open(save_path, 'wb') as destination:
            for chunk in dxf_file.chunks():
                destination.write(chunk)
        # Get data from the DXF file
        # ------------------------------------------------------
                
        # ------------------------------------------------------
        unit = request.POST.get('unit')
        current_unit = units_model.objects.create(unit=unit)
        context = {'current_unit':current_unit}
        return render(request, 'block-params.html', context)
    units = units_model
    context = {'units':units}
    return render(request, 'home.html', context)

def params1(request):
    units = units_model.objects.all()
    context = {'units', units}
    return render(request, 'block-params.html', context)

def cancel(request):
    models = [units_model, block_model, door_model, window_model, opening_model]
    for model in models:
        model.objects.all().delete()
    return redirect('home')

def add_block_type(request):
    width = request.POST.get('width')
    height = request.POST.get('height')
    length = request.POST.get('length')
    layer = request.POST.get('layer-name')
    new_block = block_model.objects.create(
            width=width,
            height=height,
            length=length,
            layer=layer
        )
    return redirect('block-params')

def params2(request):
    return render(request, 'door-params.html')

def params3(request):
    return render(request, 'window-params.html')

def params4(request):
    return render(request,'openings-params.html')

def details(request):
    return render(request, 'details.html')