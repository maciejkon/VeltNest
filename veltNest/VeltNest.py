import nest2D
import svgpathtools
import shutil

import Database
import Database as Db


class NestingApp:

    @classmethod
    def get_points_from_database(cls):
        points = Db.getPoints()
        list_of_points = list(points.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(" ","").replace("'", "").split(","))
        return list_of_points

    @classmethod
    def get_numberOfElements_from_database(cls):
        number = Db.getNumberOfElements()
        number = number.replace("[(","").replace(",)]","")
        return int(number)

    @classmethod
    def add_number_of_elements_to_Database(cls, number):
        Db.addNumberOfElements(number)

    @classmethod
    def get_and_parse(cls, nameOfSvgFile):
        Db.cleanDb()
        Db.addPath(nameOfSvgFile)
        cls.parse_path(cls.get_svg_file(nameOfSvgFile))

    @classmethod
    def get_svg_file(cls, nameOfSvgFile):
        paths, attributes, svg_attributes = svgpathtools.svg2paths2(nameOfSvgFile)
        return paths

    @classmethod
    def parse_path(cls, path):
        raw_list_of_points = str(path[0].d()).replace("M", "").replace("L", "").replace("  ", ",").split(",")
        final_list_of_points = []
        for x in range(0, 10):
            item = float(raw_list_of_points[x])
            final_list_of_points.append(item*100000)
        Database.addPoints(str(final_list_of_points))
        #return str(final_list_of_points)

    @classmethod
    def add_figure(cls, number_of_figures_to_nest, list_of_points, items):
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

    @classmethod
    def start_app(cls, list_of_points, number_of_elements):
        original_outfile_path = r'C:\Users\macie\PycharmProjects\VeltNest\endFile.svg'
        target_outfile_path = r'C:\Users\macie\PycharmProjects\VeltNest\end\endFile.svg'

        input = []
        box = nest2D.Box(1200000000, 800000000)

        cls.add_figure(number_of_elements, list_of_points, input)

        pgrp = nest2D.nest(input, box)

        sw = nest2D.SVGWriter()
        sw.write_packgroup(pgrp)
        sw.save()

        try:
            shutil.move(original_outfile_path, target_outfile_path)
            print(f"Plik końcowy został utworzony w {target_outfile_path}")
            Db.cleanDb()
        except FileNotFoundError:
            print("Proces nestingu zakończył się niepowodzeniem")

#sprawdzanie nestingu lokalnie bez GUI
# def start_app():
#
#     original_outfile_path = r'C:\Users\macie\PycharmProjects\VeltNest\endFile.svg'
#     target_outfile_path = r'C:\Users\macie\PycharmProjects\VeltNest\end\endFile.svg'
#
#     name = 'C:/Users/macie/PycharmProjects/VeltNest/start/prostokat.svg'
#     path = NestingApp.get_svg_file(name)
#     points = NestingApp.parse_path(path)
#     numberOfElementsToNest = 15
#
#     input = []
#     # wymiary powierzchni roboczej lasera
#     box = nest2D.Box(1200000000, 800000000)
#
#     NestingApp.add_figure(numberOfElementsToNest, points, input)
#
#     pgrp = nest2D.nest(input, box)
#
#     sw = nest2D.SVGWriter()
#     sw.write_packgroup(pgrp)
#     sw.save()
#
#     try:
#         shutil.move(original_outfile_path, target_outfile_path)
#         print(f"Plik końcowy został utworzony w {target_outfile_path}")
#     except FileNotFoundError:
#         print("Proces nestingu zakończył się niepowodzeniem")
#
#
# if __name__ == '__main__':
#     start_app()
