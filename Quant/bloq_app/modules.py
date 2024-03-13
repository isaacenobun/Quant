import sys
ezdxf_path = '/Users/user/Desktop/Repos/Quant/Env/lib/python3.10/site-packages'
sys.path.append(ezdxf_path)
import ezdxf

def get_line_length(line):
    return (line.dxf.end - line.dxf.start).magnitude

def separate_lines(lines, threshold):
    return [line for line in lines if get_line_length(line) > threshold]

def group_Vlines(lines, distance_threshold):
    # Sort the lines by length from longest to shortest
    lines = sorted(lines, key=lambda line: abs(line.dxf.start[1] - line.dxf.end[1]), reverse=True)
    groups = []
    
    while len(lines) > 0:
        current_line = lines.pop(0)
        span_start = min(current_line.dxf.start[1], current_line.dxf.end[1])
        span_end = max(current_line.dxf.start[1], current_line.dxf.end[1])
        group = [current_line]
        remaining_lines = []
        for line in lines:
            if (min(line.dxf.start[1], line.dxf.end[1]) >= span_start and max(line.dxf.start[1], line.dxf.end[1]) <= span_end) or \
               (min(line.dxf.start[1], line.dxf.end[1]) <= span_start and max(line.dxf.start[1], line.dxf.end[1]) >= span_start) or \
               (min(line.dxf.start[1], line.dxf.end[1]) <= span_end and max(line.dxf.start[1], line.dxf.end[1]) >= span_end):
                if 50 < abs(current_line.dxf.start[0] - line.dxf.start[0]) < distance_threshold:
                    group.append(line)
                else:
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        groups.append(group)
        
        # Check if the group has only one line
        if len(group) == 1:
            single_line = group[0]
            for line in lines:
                if 50 < abs(single_line.dxf.start[0] - line.dxf.start[0]) < distance_threshold:
                    group.append(line)
                    remaining_lines.remove(line)  # Remove line from remaining lines
            groups.pop()  # Remove the single-line group
        
        lines = remaining_lines
    
    return groups

def group_Hlines(lines, distance_threshold):
    # Sort the lines by length from longest to shortest
    lines = sorted(lines, key=lambda line: abs(line.dxf.start[0] - line.dxf.end[0]), reverse=True)
    groups = []
    
    while len(lines) > 0:
        current_line = lines.pop(0)
        span_start = min(current_line.dxf.start[0], current_line.dxf.end[0])
        span_end = max(current_line.dxf.start[0], current_line.dxf.end[0])
        group = [current_line]
        remaining_lines = []
        for line in lines:
            if (min(line.dxf.start[0], line.dxf.end[0]) >= span_start and max(line.dxf.start[0], line.dxf.end[0]) <= span_end) or \
               (min(line.dxf.start[0], line.dxf.end[0]) <= span_start and max(line.dxf.start[0], line.dxf.end[0]) >= span_start) or \
               (min(line.dxf.start[0], line.dxf.end[0]) <= span_end and max(line.dxf.start[0], line.dxf.end[0]) >= span_end):
                if 50 < abs(current_line.dxf.start[1] - line.dxf.start[1]) < distance_threshold:
                    group.append(line)
                else:
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        groups.append(group)
        
        # Check if the group has only one line
        if len(group) == 1:
            single_line = group[0]
            for line in lines:
                if 50 < abs(single_line.dxf.start[1] - line.dxf.start[1]) < distance_threshold:
                    group.append(line)
                    remaining_lines.remove(line)  # Remove line from remaining lines
            groups.pop()  # Remove the single-line group
        
        lines = remaining_lines
    
    return groups

def find_walls(file_path, layer_name, threshold):
    horizontal_walls = []
    vertical_walls = []
    dwg = ezdxf.readfile(file_path)
    modelspace = dwg.modelspace()

    # Get all lines in the specified layer
    lines = list(modelspace.query(f'LINE[layer=="{layer_name}"]'))

    # Separate lines into horizontal and vertical
    horizontal_lines = [line for line in lines if abs(line.dxf.start[0] - line.dxf.end[0]) > abs(line.dxf.start[1] - line.dxf.end[1])]
    vertical_lines = [line for line in lines if line not in horizontal_lines]

    # print("Total number of lines:", len(lines))
    # print("\nNumber of horizontal lines:", len(horizontal_lines))
    # print("Number of vertical lines:", len(vertical_lines))

    # Discard lines shorter than threshold
    horizontal_lines = separate_lines(horizontal_lines, threshold)
    vertical_lines = separate_lines(vertical_lines, threshold)

    # print("\nNumber of horizontal lines after filtering:", len(horizontal_lines))
    # print("Number of vertical lines after filtering:", len(vertical_lines))

    # Group horizontal lines
    horizontal_groups = group_Hlines(horizontal_lines, threshold)

    # print("\nNumber of horizontal groups:", len(horizontal_groups))
    # for i, group in enumerate(horizontal_groups, start=1):
    #     print(f"Horizontal Group {i}: {len(group)} lines")

    # Group vertical lines
    vertical_groups = group_Vlines(vertical_lines, threshold)

    # print("\nNumber of vertical groups:", len(vertical_groups))
    # for i, group in enumerate(vertical_groups, start=1):
    #     print(f"Vertical Group {i}: {len(group)} lines")

    # Pick the longest line from each group to represent a wall
    for group in horizontal_groups:
        horizontal_walls.append(max(group, key=get_line_length))

    for group in vertical_groups:
        vertical_walls.append(max(group, key=get_line_length))

    return horizontal_walls, vertical_walls

def walls_output(file_path,layer_name,threshold):
    # file_path = "/Users/user/Downloads/new-sample.dxf"
    # layer_name = "A-WALL"
    # threshold = 250  # Threshold for discarding short lines

    # Find horizontal and vertical walls
    horizontal_walls, vertical_walls = find_walls(file_path, layer_name, threshold)

    # Output horizontal walls
    # print("\nHorizontal Walls:")
    # for i, wall in enumerate(horizontal_walls, start=1):
    #     print(f"Wall {i}: Length = {get_line_length(wall):.2f}mm")

    # Output vertical walls
    # print("\nVertical Walls:")
    # for i, wall in enumerate(vertical_walls, start=1):
    #     print(f"Wall {i}: Length = {get_line_length(wall):.2f}mm")

    # Output total number of walls
    total_walls = len(horizontal_walls) + len(vertical_walls)
    # print(f"\nTotal number of walls: {total_walls}")

    return total_walls