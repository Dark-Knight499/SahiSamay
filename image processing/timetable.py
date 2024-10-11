import easyocr
import utils_tt
import tableextractor


def get_tt(image_path):
    tt = utils_tt.initialize()

    te = tableextractor.TableExtractor(image_path)
    img = te.execute()

    reader = easyocr.Reader(['en'], gpu=False)
    text = reader.readtext(img)
    for i in text:
        print(i)
    rows = utils_tt.sort_row(text)
    cell_height = utils_tt.mean_cell_height(rows[0])
    start_height = utils_tt.start_point(text)

    days = rows[1:]

    utils_tt.assign_loop(tt, days, start_height, cell_height)
    utils_tt.assign_ipd(tt)
    print(tt)
    return tt

