import os
import xml.etree.ElementTree as ET

# Class mapping
class_map = {
    'ore carrier': 0,
    'general cargo ship': 1,
    'bulk cargo ship': 2,
    'container ship': 3,
    'bulk cargo carrier': 4,
    'fishing boat': 5,
    'passenger ship': 6
}

def convert_xml_folder_to_yolo(xml_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for xml_file in os.listdir(xml_folder):
        if not xml_file.endswith('.xml'):
            continue

        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()

        width = int(root.find('size/width').text)
        height = int(root.find('size/height').text)

        yolo_lines = []

        for obj in root.findall('object'):
            class_name = obj.find('name').text.strip().lower()
            if class_name not in class_map:
                print(f"[WARNING] Skipping unknown class: '{class_name}' in {xml_file}")
                continue

            class_id = class_map[class_name]
            bndbox = obj.find('bndbox')

            xmin = int(float(bndbox.find('xmin').text))
            ymin = int(float(bndbox.find('ymin').text))
            xmax = int(float(bndbox.find('xmax').text))
            ymax = int(float(bndbox.find('ymax').text))

            # Convert to YOLO format (normalized)
            x_center = (xmin + xmax) / 2 / width
            y_center = (ymin + ymax) / 2 / height
            box_width = (xmax - xmin) / width
            box_height = (ymax - ymin) / height

            yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}")

        txt_filename = os.path.splitext(xml_file)[0] + '.txt'
        with open(os.path.join(output_folder, txt_filename), 'w') as out_file:
            out_file.write('\n'.join(yolo_lines))

        print(f"[OK] {xml_file} -> {txt_filename}")

# Convert datasets
convert_xml_folder_to_yolo('./train', 'train_labels')
convert_xml_folder_to_yolo('./val', 'val_labels')
convert_xml_folder_to_yolo('./test', 'test_labels')
