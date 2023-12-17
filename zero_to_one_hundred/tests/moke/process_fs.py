"""ProcessFS:
deal with Process
mocked in Test
"""


from zero_to_one_hundred.repository.process_fs import ProcessFS as _ProcessFS


class ProcessFS(_ProcessFS):
    @classmethod
    def write_img(cls, dir_img, http_url_img):
        print(f"write_img  {dir_img} {http_url_img}")

    @classmethod
    def write_epub(cls, config_map, dir_epub, isbn):
        print(f"write_epub {config_map} {dir_epub} {isbn}")
