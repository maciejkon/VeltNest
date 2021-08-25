import nest2D
import svgpathtools
import shutil


def get_svg_file(nameOfSvgFile):
    paths, attributes, svg_attributes = svgpathtools.svg2paths2(nameOfSvgFile)
    return paths

def parse_path(path):
    _MM_IN_PIXEL_UNITS = 230000
    print(path)
    raw_list_of_points = str(path[0].d()).replace("M", "").replace("L", "").replace("  ", ",").split(",")
    print(raw_list_of_points)
    final_list_of_points = []
    for x in range(0, 10):
        item = int(float(raw_list_of_points[x]))
        #final_list_of_points.append(str(item)+ "00000")
        final_list_of_points.append(item*_MM_IN_PIXEL_UNITS)
    print(final_list_of_points)
    return final_list_of_points


def add_figure(number_of_figures_to_nest, list_of_points, items):
    for i in range(number_of_figures_to_nest):
        item = nest2D.Item([
            # LG
            nest2D.Point(-int(float(list_of_points[0])), int(float(list_of_points[1]))),
            # PG
            nest2D.Point(int(float(list_of_points[2])), int(float(list_of_points[3]))),
            # PD
            nest2D.Point(int(float(list_of_points[4])), -int(float(list_of_points[5]))),
            # LD
            nest2D.Point(-int(float(list_of_points[6])), -int(float(list_of_points[7]))),
            # LG
            nest2D.Point(-int(float(list_of_points[0])), int(float(list_of_points[1]))),
        ])
        items.append(item)


def main():
    original_outfile_path = r'C:\Users\macie\PycharmProjects\VeltNest\endFile.svg'
    target_outfile_path = r'C:\Users\macie\PycharmProjects\VeltNest\end\endFile.svg'
    points = parse_path(get_svg_file('start\prostokat.svg'))


    input = []
    #wymiary powierzchni roboczej lasera
    box = nest2D.Box(1200000000, 800000000)

    add_figure(22, points, input)
    pgrp = nest2D.nest(input, box)

    sw = nest2D.SVGWriter()
    sw.write_packgroup(pgrp)
    sw.save()

    try:
        shutil.move(original_outfile_path, target_outfile_path)
        print(f"Plik końcowy został utworzony w {target_outfile_path}")
    except FileNotFoundError:
        print("Proces nestingu zakończył się niepowodzeniem")


if __name__ == '__main__':
    main()
