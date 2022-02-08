import os
import nest2D
import svgpathtools
import shutil
import Database as Db


class NestingApp:

    def check_if_database_is_empty(self, data_to_check):
        substring = "DEFAULT"
        try:
            data_to_check.index(substring)
        except ValueError:
            return False
        else:
            return True

    def check_file_format(self, name_of_file):
        svg_file_extension = ".svg"
        name, extension = os.path.splitext(name_of_file)
        try:
            extension.index(svg_file_extension)
        except ValueError:
            return False
        else:
            return True

    @classmethod
    def get_file_name(cls):
        name_of_file = Db.get_name()
        if cls.check_if_database_is_empty(cls, name_of_file):
            return False
        else:
            name_of_file = name_of_file.replace("[(", "").replace(",)]", "").replace("\'","")
            return str(name_of_file)

    @classmethod
    def get_points(cls):
        points = Db.get_points()
        if cls.check_if_database_is_empty(cls, points):
            return False
        else:
            list_of_points = list(
                points.replace("[", "").replace("]", "").replace("(", "")
                    .replace(")", "").replace(" ", "").replace(
                "'", "").split(","))
            return list_of_points

    @classmethod
    def get_number_of_elements(cls):
        number = Db.get_number_of_elements()
        if cls.check_if_database_is_empty(cls, number):
            return False
        else:
            number = number.replace("[(", "").replace(",)]", "")
            return int(number)

    @classmethod
    def set_number_of_elements(cls, number):
        try:
            if number.isdigit():
                Db.add_number_of_elements(number)
                return True
        except TypeError:
            return False

    @classmethod
    def set_file_path(cls, path):
        Db.add_path_of_file(path)

    @classmethod
    def get_svg_file(cls, name_of_svg_file):
        paths, attributes, svg_attributes = svgpathtools.svg2paths2(name_of_svg_file)
        return paths

    @classmethod
    def get_and_parse(cls):
        name_of_svg_file = cls.get_file_name()
        cls.parse_path(cls.get_svg_file(name_of_svg_file))

    @classmethod
    def parse_path(cls, path):
        scale_multiplier = 1000000
        raw_list_of_points = str(path[0].d()).replace("M", "").replace("L", "").replace("  ", ",").split(",")
        final_list_of_points = []
        for x in range(0, 10):
            item = float(raw_list_of_points[x])
            final_list_of_points.append(item*scale_multiplier)
        Db.add_points(str(final_list_of_points))

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
            Db.clean_db()
            return True
        except FileNotFoundError:
            return False


