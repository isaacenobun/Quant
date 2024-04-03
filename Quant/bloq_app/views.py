from django.shortcuts import render,redirect
from django.http import JsonResponse
import os
from django.conf import settings

from .modules import *
from .models import *

import numpy as np
import math

# Home
# -------------------------------------------------------------
def home(request):
    if request.method == 'POST' and request.FILES.get('dxf_file'):
        dxf_file = request.FILES['dxf_file']
        save_path = os.path.join(settings.BASE_DIR, '/Users/user/Desktop/Repos/Quant/Quant/bloq_app/static/dxf_files', dxf_file.name)
        with open(save_path, 'wb') as destination:
            for chunk in dxf_file.chunks():
                destination.write(chunk)
        
        save_wall_door_layer_plot(save_path,'plot.png')
        
        move_file_if_exists('plot.png', '/Users/user/Desktop/Repos/Quant/Quant', '/Users/user/Desktop/Repos/Quant/Quant/bloq_app/static/plot_images')
        
        # Get data from the DXF file
        unit = request.POST.get('unit')
        current_unit = units_model.objects.create(unit=unit)
        context = {'current_unit':current_unit}
        return render(request, 'block-params.html', context)
    units = units_model
    context = {'units':units}
    return render(request, 'home.html', context)

# Blocks
# -------------------------------------------------------------
def params1(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_blocks = block_model.objects.all()
    context = {'current_unit': current_unit, 'existing_blocks': existing_blocks}
    return render(request, 'block-params.html', context)

def params1_edit(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_blocks = block_model.objects.all()
    context = {'current_unit': current_unit, 'existing_blocks': existing_blocks}
    return render(request, 'block-params-edit.html', context)

def add_block_type(request):
    width = request.POST.get('width')
    height = request.POST.get('height')
    length = request.POST.get('length')
    layer = request.POST.get('layer')
    new_block = block_model.objects.create(
        width=width,
        height=height,
        length=length,
        layer=layer
    )
    return redirect('block-params')

def add_block_type_edit(request):
    width = request.POST.get('width')
    height = request.POST.get('height')
    length = request.POST.get('length')
    layer = request.POST.get('layer')
    new_block = block_model.objects.create(
        width=width,
        height=height,
        length=length,
        layer=layer
    )
    return redirect('block-params-edit')

def delete_block_type(request,blockId):
    block_id = blockId
    block = block_model.objects.get(pk=block_id)
    block.delete()
    return redirect('block-params')

def delete_block_type_edit(request,blockId):
    block_id = blockId
    block = block_model.objects.get(pk=block_id)
    block.delete()
    return redirect('block-params-edit')

# Doors
# -------------------------------------------------------------
def params2(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_doors = door_model.objects.all()
    context = {'current_unit': current_unit, 'existing_doors': existing_doors}
    return render(request, 'door-params.html', context)

def params2_edit(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_doors = door_model.objects.all()
    context = {'current_unit': current_unit, 'existing_doors': existing_doors}
    return render(request, 'door-params-edit.html', context)

def add_door_type(request):
    width = request.POST.get('width')
    height = request.POST.get('height')
    quantity = request.POST.get('quantity')
    new_door = door_model.objects.create(
        width=width,
        height=height,
        quantity=quantity
    )
    return redirect('door-params')

def add_door_type_edit(request):
    width = request.POST.get('width')
    height = request.POST.get('height')
    quantity = request.POST.get('quantity')
    new_door = door_model.objects.create(
        width=width,
        height=height,
        quantity=quantity
    )
    return redirect('door-params-edit')

def delete_door_type(request,doorId):
    door_id = doorId
    door = door_model.objects.get(pk=door_id)
    door.delete()
    return redirect('door-params')

def delete_door_type_edit(request,doorId):
    door_id = doorId
    door = door_model.objects.get(pk=door_id)
    door.delete()
    return redirect('door-params-edit')

# Windows
# -------------------------------------------------------------
def params3(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_windows = window_model.objects.all()
    context = {'current_unit': current_unit, 'existing_windows': existing_windows}
    return render(request, 'window-params.html', context)

def params3_edit(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_windows = window_model.objects.all()
    context = {'current_unit': current_unit, 'existing_windows': existing_windows}
    return render(request, 'window-params-edit.html', context)

def add_window_type(request):
    width = request.POST.get('width')
    height = request.POST.get('height')
    quantity = request.POST.get('quantity')
    new_window = window_model.objects.create(
        width=width,
        height=height,
        quantity=quantity
    )
    return redirect('window-params')

def add_window_type_edit(request):
    width = request.POST.get('width')
    height = request.POST.get('height')
    quantity = request.POST.get('quantity')
    new_window = window_model.objects.create(
        width=width,
        height=height,
        quantity=quantity
    )
    return redirect('window-params-edit')

def delete_window_type(request,windowId):
    window_id = windowId
    window = window_model.objects.get(pk=window_id)
    window.delete()
    return redirect('window-params')

def delete_window_type_edit(request,windowId):
    window_id = windowId
    window = window_model.objects.get(pk=window_id)
    window.delete()
    return redirect('window-params-edit')

# Openings
# -------------------------------------------------------------
def params4(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_openings = opening_model.objects.all()
    context = {'current_unit': current_unit, 'existing_openings': existing_openings}
    return render(request, 'opening-params.html', context)

def params4_edit(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()
    existing_openings = opening_model.objects.all()
    context = {'current_unit': current_unit, 'existing_openings': existing_openings}
    return render(request, 'opening-params-edit.html', context)

def add_opening_type(request):
    area = request.POST.get('area')
    quantity = request.POST.get('quantity')
    new_window = opening_model.objects.create(
        area=area,
        quantity=quantity
    )
    return redirect('opening-params')

def add_opening_type_edit(request):
    area = request.POST.get('area')
    quantity = request.POST.get('quantity')
    new_window = opening_model.objects.create(
        area=area,
        quantity=quantity
    )
    return redirect('opening-params-edit')

def delete_opening_type(request,openingId):
    opening_id = openingId
    opening = opening_model.objects.get(pk=opening_id)
    opening.delete()
    return redirect('opening-params')

def delete_opening_type_edit(request,openingId):
    opening_id = openingId
    opening = opening_model.objects.get(pk=opening_id)
    opening.delete()
    return redirect('opening-params-edit')

# Details
# -------------------------------------------------------------
def details(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()

    blocks = block_model.objects.all()
    doors = door_model.objects.all()
    windows = window_model.objects.all()
    openings = opening_model.objects.all()

    context = {'current_unit':current_unit, 'blocks':blocks,'doors':doors,'windows':windows,'openings':openings}

    return render(request, 'details.html', context)


# Report
# -------------------------------------------------------------
def report(request):
    current_unit = units_model.objects.all()
    if not current_unit:
        current_unit = units_model.objects.create(unit='mm')
    else:
        current_unit = current_unit.first()

    blocks = block_model.objects.all()
    doors = door_model.objects.all()
    windows = window_model.objects.all()
    openings = opening_model.objects.all()

    height = int(request.POST.get('height'))

    # calculations
    # -------------------------------------------------------------

    save_path = os.path.join(settings.BASE_DIR, '/Users/user/Desktop/Repos/Quant/Quant/bloq_app/static/dxf_files', 'sample-4.dxf')

    wall_block = {block.layer: walls_output(save_path, block.layer, 225) for block in blocks}

    dxf_door_no = count_doors_in_layer(save_path)

    input_door_no,door_area,door_space =  get_door_info(doors,height)

    window_area = 0
    for window in windows:
        window_area += window.width*window.height*window.quantity

    openings_area = 0
    for opening in openings:
        openings_area += opening.area*opening.quantity
    
    wall_lengths, wall_areas, node_areas, H_mortar_areas, V_mortar_areas = [],[],[], [], []
    for block in blocks:
        wall_length = int(get_walls_length(save_path,block.layer,block.width))
        node_area = calculate_nodes(save_path,block.layer) * block.width*height
        wall_lengths.append(wall_length)
        wall_areas.append(wall_length*height)
        node_areas.append(node_area)

        # Mortar technicalities

        H_mortar_lines = height/block.height
        H_mortar_areas.append(H_mortar_lines * 9.53 * wall_length)

        V_mortar_lines = (wall_length/block.length)/2
        V_mortar_areas.append(V_mortar_lines * 9.53 * (height-(25*H_mortar_lines)))

    total_node_area = sum(np.array(node_areas))

    total_wall_length = sum(np.array(wall_lengths))

    total_area = sum(np.array(wall_areas)) - openings_area + door_space - window_area - sum(np.array(node_areas)) - sum(np.array(H_mortar_areas)) - sum(np.array(V_mortar_areas))

    ratio = np.array(wall_areas)/min(np.array(wall_areas))

    new_total_areas = []
    for i in ratio:
        new_total_areas.append(i/sum(ratio) * total_area)
    
    block_no = []
    count=0
    for area in new_total_areas:
        block_no.append(math.ceil((area/((blocks[count].length)*(blocks[count].height)))))
        # block_multiple = 9.88/10**6
        # block_no.append(math.ceil(area*block_multiple))
        count=+1
    
    total_blocks = sum(np.array(block_no))
        
    context = {'current_unit':current_unit, 'blocks':blocks,'doors':doors,'windows':windows,'openings':openings,'height':height,'wall_block':wall_block, 'dxf_door_no':dxf_door_no, 'input_door_no':input_door_no, 'door_area':door_area, 'door_space':door_space, 'window_area':window_area, 'openings_area':openings_area, 'wall_areas':wall_areas, 'block_no':block_no, 'total_blocks':total_blocks, 'total_wall_length':total_wall_length, 'total_node_area':total_node_area}

    return render(request, 'report.html', context)


# Cancel
# -------------------------------------------------------------
def cancel(request):
    models = [units_model, block_model, door_model, window_model, opening_model]
    for model in models:
        model.objects.all().delete()
    return redirect('home')