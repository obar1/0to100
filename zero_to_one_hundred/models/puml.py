import os
from typing import List

from configs.config import ConfigMap
from models.section import Section


class PUML:
    def __init__(self, config_map: ConfigMap, PersistFS, sections: List[Section]):
        self.config_map = config_map
        self.readme_puml = config_map.get_repo_path + '/' + config_map.get_repo_readme_puml
        self.PersistFS = PersistFS
        self.sections = sections

    # @startmindmap
    #
    # * Solving \n Global \n Warming
    #  * Eating differently
    #   * Vegan
    #   * Vegetarian
    #   * Less processed foods
    #   * Buy local food
    #  * Travel
    #   * Bike more
    #   * Ride buses
    #   * Buy an electric car
    #
    #  * Home
    #   *_ Energy audit
    #   *_ Use a cloths line
    #   *_ Add insulation
    #   *_ Get solar panels
    #  * Be a role model
    #   *_ Vote
    #   *_ Encourage others
    #   *_ Teach your kids
    #
    # @endmindmap

    def __repr__(self):
        return f"Map {self.readme_puml}, {self.sections}"

    def __repr_flatten(self, rows: List[Section]) -> str:
        # 1. <https://cloud.google.com/api-gateway/docs/about-ap
        # i-gateway> :ok: [`here`](../https:§§cloud.google.com§api-gateway§docs§about-api-gateway/readme.md)

        lambda_flatten_section = lambda s: ' * ' + s.get_dir_name
        rows = sorted(list(map(lambda_flatten_section, rows)))

        for f in range(len(rows)):
            # print('\n>'+str(f)+rows[f])
            for b in range(f + 1, len(rows)):
                # print('='+str(b)+rows[b])
                if str(rows[b]).startswith(str(rows[f])):
                    rows[b] = str(rows[b]).replace(str(rows[f]), '  * ')
                # else:
                #     print('*'+str(rows[f]))

        for f in range(len(rows)):
            print(rows[f])
        return os.linesep.join(rows)

    def write(self):
        # init with list of sections found
        txt = []
        txt.append("""
@startmindmap puml
* root
{}

@endmindmap
        """.format(self.__repr_flatten(self.sections)))
        return self.PersistFS.write_file(self.readme_puml, txt)
