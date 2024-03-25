Search.setIndex({"docnames": ["dev_guide/developer_guide", "index", "user_guide/app_settings", "user_guide/data_io", "user_guide/getting_started", "user_guide/image_preprocessing", "user_guide/modules", "user_guide/registration", "user_guide/segmentation", "user_guide/user_interface"], "filenames": ["dev_guide/developer_guide.rst", "index.rst", "user_guide/app_settings.rst", "user_guide/data_io.rst", "user_guide/getting_started.rst", "user_guide/image_preprocessing.rst", "user_guide/modules.rst", "user_guide/registration.rst", "user_guide/segmentation.rst", "user_guide/user_interface.rst"], "titles": ["Developer Guide", "Welcome to MRIphantom QA Solution\u2019s documentation!", "Application Settings", "Data Loading and Saving", "Getting Started", "Image Preprocessing", "Modules", "Image Registration", "Image Segmentation", "User Interface"], "terms": {"index": 1, "modul": 1, "search": 1, "page": [1, 4], "i": [0, 1, 3, 4, 5, 7, 8], "python": [1, 4], "softwar": [1, 4, 7, 8], "automat": [1, 7], "analysi": [1, 4, 5], "mri": [0, 1, 4, 8], "imag": [0, 1, 4], "us": [0, 1, 5, 7, 8], "radiotherapi": 1, "plan": 1, "thi": [0, 1, 3, 4, 5, 8], "allow": [0, 1], "you": [0, 1, 3, 4, 5], "quickli": 1, "easili": 1, "analyz": [0, 1], "geometr": 1, "distort": 1, "project": [0, 1, 4], "under": 1, "activ": [1, 4], "develop": [1, 3, 4, 9], "so": [0, 1], "care": 1, "when": 1, "program": 1, "To": [0, 4], "mriphantom": 0, "first": 4, "clone": 4, "repositori": 4, "your": [0, 4], "local": [0, 4], "machin": 4, "git": 4, "gitlab": 4, "com": 4, "bzavolovich": 4, "mriphantom_desktop": [0, 4], "make": 4, "sure": 4, "have": [0, 4, 8], "latest": 4, "version": 1, "creat": 4, "virtual": 4, "environ": 4, "directori": [0, 4], "run": [0, 4], "follow": [0, 4], "command": [0, 4], "m": 4, "venv": 4, "linux": 4, "maco": 4, "script": 4, "window": [1, 4], "ps1": 4, "necessari": 4, "packag": 4, "requir": [1, 8], "txt": 4, "pip": [0, 4], "r": 4, "applic": [0, 1, 4, 9], "execut": [0, 4, 5], "app": [0, 4], "py": 4, "usag": [], "instal": [0, 1], "from": [0, 1, 8], "sourc": 1, "get": 1, "start": 1, "system": [0, 1], "oper": [0, 1, 5], "hardwar": 1, "configur": [0, 1], "min": [], "learn": [], "basic": 1, "welcom": 4, "contain": [0, 4, 5], "instruct": [1, 4], "should": [0, 4], "compat": 4, "modern": 4, "howev": 4, "mai": [0, 4], "encount": 4, "issu": 4, "older": 4, "particularli": 4, "those": 4, "8": 4, "1": [0, 4, 5], "earlier": 4, "10": 4, "11": 4, "big": 4, "sur": 4, "later": 4, "both": [4, 8], "appl": 4, "silicon": 4, "intel": 4, "base": [0, 4, 8], "comput": [0, 4], "ani": 4, "recent": 4, "lt": 4, "distribut": 4, "exampl": [4, 5, 8], "ubuntu": 4, "18": 4, "04": 4, "memori": 4, "At": [3, 4], "least": 4, "4gb": 4, "ram": 4, "displai": 4, "A": [0, 4, 8], "minimum": [0, 4], "resolut": [1, 4], "1024": 4, "x": [0, 4], "768": 4, "fullhd": 4, "recommend": 4, "graphic": 4, "dedic": [4, 8], "gpu": [4, 8], "faster": 4, "render": 4, "io": 4, "devic": 4, "standard": [0, 4], "mous": 4, "keyboard": 4, "internet": 4, "connect": 4, "Not": 4, "moment": [3, 4], "current": [4, 7, 8], "its": [0, 4], "earli": 4, "stage": 4, "offer": [], "straightforward": 8, "yet": [], "promis": [], "set": 1, "featur": [], "while": [], "complex": [], "navig": [], "through": [], "function": 0, "can": [0, 3, 4, 5], "still": [], "confus": [], "here": 4, "": [0, 4, 8], "how": [0, 4], "refer": 4, "document": 4, "readm": 4, "file": [0, 3, 4, 5], "user": 1, "interfac": 1, "main": [1, 5], "new": [], "studi": [], "visual": 1, "3d": [0, 1], "viewer": [0, 1], "2d": [0, 1], "histogram": [0, 1], "heatmap": 1, "statist": [0, 1], "data": [0, 1, 5], "load": [0, 1], "save": [0, 1, 4, 5], "import": [0, 1], "export": [0, 1, 5], "preprocess": 1, "origin": 1, "interpol": [0, 1], "better": 1, "qualiti": 1, "detect": 1, "segment": [1, 5], "threshold": [0, 1, 5], "overview": [1, 9], "guid": 1, "build": 1, "debug": 1, "style": 1, "registr": 1, "process": [0, 5, 8], "provid": 0, "marker": [0, 5], "slice_img_gener": [0, 1], "input_fil": 0, "fals": 0, "perform_threshold": [0, 1], "img_gen": 0, "is_mri": 0, "isolate_mark": [0, 1], "threshold_gen": 0, "save_path": 0, "count_differ": [0, 1], "ct_path": 0, "mri_path": 0, "get_coord": [0, 1], "markers_path": 0, "src": 0, "count": 0, "differ": [0, 8], "between": [0, 8], "ct": [0, 4, 8], "calcul": [0, 4], "coordin": [0, 5], "It": [0, 8], "variou": 0, "mean": 0, "maximum": 0, "deviat": 0, "number": 0, "exceed": 0, "certain": 0, "0": 0, "5": 0, "mm": 0, "The": 0, "result": [0, 5], "ar": [0, 4, 5, 8], "json": 0, "overal": 0, "per": 0, "slice": [0, 5], "paramet": 0, "string": 0, "specifi": 0, "path": 0, "pickl": [0, 5], "where": 0, "return": 0, "param": 0, "dictionari": 0, "distanc": 0, "an": 0, "arrai": 0, "all": [0, 4, 5], "slice_dist": 0, "retriev": 0, "read": 0, "locat": 0, "given": 0, "extract": 0, "numpi": 0, "repres": 0, "each": 0, "y": 0, "z": 0, "list": 0, "inner": 0, "format": [0, 3, 4], "isol": [0, 5], "gener": 1, "appli": [0, 5], "filter": 0, "morpholog": 0, "yield": 0, "boolean": 0, "indic": 0, "whether": 0, "default": 0, "none": 0, "perform": 0, "techniqu": [0, 8], "valu": [0, 8], "option": [0, 8], "output": 0, "e": 0, "g": 0, "nii": [0, 3, 4], "after": 0, "includ": 0, "intens": [0, 8], "normal": 0, "resiz": 0, "input": [0, 5], "entranc": 1, "unpack": [0, 5], "dicom_to_nifti": [0, 1], "source_fold": 0, "target_fold": 0, "name": 0, "convert": 0, "folder": 0, "dicom": [0, 3, 4], "gz": [0, 3, 4], "adjust_data": [], "img": [], "mask": 5, "flag_multi_class": [], "num_class": [], "genetrainnpi": [], "image_path": [], "mask_path": [], "2": [0, 5], "image_prefix": [], "mask_prefix": [], "image_as_grai": [], "true": [], "mask_as_grai": [], "label_visu": [], "color_dict": [], "save_result": [], "npyfil": [], "test2_dataset_gener": [], "test_path": [], "target_s": [], "512": [], "as_grai": [], "test_dataset_gener": [], "256": [], "train_gener": [], "batch_siz": [], "train_path": [], "image_fold": [], "mask_fold": [], "aug_dict": [], "image_color_mod": [], "grayscal": [], "mask_color_mod": [], "image_save_prefix": [], "mask_save_prefix": [], "save_to_dir": [], "seed": [], "same": [], "time": [], "image_datagen": [], "mask_datagen": [], "ensur": 0, "transform": [], "want": [], "class": 0, "d": [], "titl": 0, "\u0433\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u0430": 0, "\u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0439": 0, "plot": [0, 1], "\u0433\u0440\u0430\u0444\u0438\u043a\u0438": 0, "scatter2d": [0, 1], "data_ct": 0, "data_mri": 0, "\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440": 0, "scatter3d": [0, 1], "tabl": 0, "header": 0, "std": 0, "\u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430": 0, "path_ct": 0, "path_mri": 0, "neural": 1, "network": 1, "section": 3, "give": 3, "inform": 3, "support": [3, 4, 7], "extens": 3, "onli": [3, 8], "avail": [3, 5, 8], "report": 3, "csv": 3, "consist": [], "one": [], "which": 5, "simpl": [], "manner": [], "need": 4, "elekta": 4, "phantom": [4, 5], "our": [4, 8], "preregist": [], "we": [4, 5], "soon": 4, "implement": 4, "simpli": 4, "press": [], "two": 5, "method": [0, 5, 8], "either": 5, "work": [0, 4, 5], "quick": 5, "choos": 5, "improv": 5, "even": [], "further": [], "select": 5, "scale": 5, "factor": 5, "upscal": 5, "initi": [0, 5], "enabl": [0, 5], "algorithm": 5, "higher": 5, "precis": 5, "finer": 5, "outcom": 5, "pipelin": [5, 8], "divid": 5, "sever": 5, "step": [0, 5, 8], "begin": 5, "scan": [5, 8], "case": [5, 8], "3": 5, "accord": 5, "leav": 5, "central": 5, "portion": 5, "plastic": [5, 8], "rod": [5, 8], "emploi": 5, "elimin": 5, "except": 5, "conduct": [4, 5], "also": 5, "look": 5, "below": [5, 8], "todo": [0, 2, 5, 8], "pictur": [5, 8], "pleas": 7, "third": [0, 7], "parti": [0, 7], "manual": 7, "regist": [4, 7], "itk": 7, "snap": 7, "etc": 7, "crucial": 8, "singl": 8, "simplest": 8, "quickest": 8, "doesn": 8, "t": [0, 8], "sinc": 8, "approach": 8, "separ": 8, "background": 8, "pixel": 8, "chosen": 8, "modal": 8, "whose": 8, "abov": 8, "classifi": 8, "belong": 8, "region": 8, "interest": 8, "respect": 8, "effect": 8, "clear": 8, "object": 8, "170": 8, "255": 8, "215": 8, "insert": 8, "pre": 4, "click": 4, "button": 4, "input_data": 0, "widget": 0, "init_histogram": [0, 1], "init_plot": [0, 1], "scatter": 0, "view": 0, "init_scatter2d": [0, 1], "z_valu": 0, "init_scatter3d": [0, 1], "init_t": [0, 1], "pyinstal": 0, "spec": 0, "If": 0, "haven": 0, "alreadi": 0, "do": 0, "via": 0, "rood": 0, "bundl": 0, "onc": 0, "check": 0, "termin": 0, "prompt": 0, "complet": 0, "find": 0, "dist": 0, "within": 0, "exact": 0, "vari": 0, "depend": 0, "test": 0, "befor": 0, "good": 0, "idea": 0, "correctli": 0, "verifi": 0, "expect": 0, "special": 0, "mode": 0, "variabl": 0, "disabl": 0, "splash": 0, "screen": 0, "other": 0, "excess": 0, "line": 0, "length": 0, "prefer": 0, "keep": 0, "shorter": 0, "than": 0, "100": 0, "charact": 0, "alwai": 0, "120": 0, "markdown": 0, "md": 0, "exclud": 0, "restrict": 0, "edit": 0, "text": 0, "without": 0, "worri": 0, "about": 0, "break": 0, "pylint": 0, "flake8": 0, "relat": 0, "specif": 0, "comment": 0, "up": 0, "date": 0, "mark": 0, "code": 0, "part": 0, "revisit": 0, "fixm": 0, "fix": 0, "graph": 1, "toolkit": 1, "librari": 1, "docstr": 1, "html": 3, "In": 9}, "objects": {"MRIphantom_desktop.src.preprocess": [[0, 0, 0, "-", "unpack"]], "MRIphantom_desktop.src.preprocess.unpack": [[0, 1, 1, "", "dicom_to_nifti"]], "MRIphantom_desktop.src.segmentation": [[0, 0, 0, "-", "process"]], "MRIphantom_desktop.src.segmentation.process": [[0, 1, 1, "", "count_difference"], [0, 1, 1, "", "get_coords"], [0, 1, 1, "", "isolate_markers"], [0, 1, 1, "", "perform_thresholding"], [0, 1, 1, "", "slice_img_generator"]], "MRIphantom_desktop.src.visualization": [[0, 0, 0, "-", "histogram"], [0, 0, 0, "-", "plots"], [0, 0, 0, "-", "scatter2d"], [0, 0, 0, "-", "scatter3d"], [0, 0, 0, "-", "table"], [0, 0, 0, "-", "viewer"]], "MRIphantom_desktop.src.visualization.histogram": [[0, 2, 1, "", "Histogram"]], "MRIphantom_desktop.src.visualization.histogram.Histogram": [[0, 3, 1, "", "init_histogram"]], "MRIphantom_desktop.src.visualization.plots": [[0, 2, 1, "", "Plots"]], "MRIphantom_desktop.src.visualization.plots.Plots": [[0, 3, 1, "", "init_plots"]], "MRIphantom_desktop.src.visualization.scatter2d": [[0, 2, 1, "", "Scatter2D"]], "MRIphantom_desktop.src.visualization.scatter2d.Scatter2D": [[0, 3, 1, "", "init_scatter2d"]], "MRIphantom_desktop.src.visualization.scatter3d": [[0, 2, 1, "", "Scatter3D"]], "MRIphantom_desktop.src.visualization.scatter3d.Scatter3D": [[0, 3, 1, "", "init_scatter3d"]], "MRIphantom_desktop.src.visualization.table": [[0, 2, 1, "", "Table"]], "MRIphantom_desktop.src.visualization.table.Table": [[0, 3, 1, "", "init_table"]], "MRIphantom_desktop.src.visualization.viewer": [[0, 2, 1, "", "Viewer"]]}, "objtypes": {"0": "py:module", "1": "py:function", "2": "py:class", "3": "py:method"}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "function", "Python function"], "2": ["py", "class", "Python class"], "3": ["py", "method", "Python method"]}, "titleterms": {"welcom": 1, "mriphantom": [1, 4], "qa": [1, 4], "solut": [1, 4], "": 1, "document": 1, "indic": 1, "tabl": [1, 9], "usag": [], "instal": 4, "from": 4, "sourc": 4, "get": 4, "start": 4, "system": 4, "requir": 4, "oper": 4, "version": 4, "hardwar": 4, "configur": 4, "min": [], "us": 4, "learn": [], "basic": 4, "data": 3, "load": 3, "save": 3, "import": 3, "export": 3, "imag": [5, 7, 8], "preprocess": [0, 5], "origin": 5, "resolut": 5, "interpol": 5, "better": 5, "qualiti": 5, "detect": 5, "segment": [0, 8], "threshold": 8, "user": 9, "interfac": 9, "main": 9, "window": 9, "new": [], "studi": [], "page": [], "visual": [0, 9], "3d": 9, "viewer": 9, "2d": 9, "histogram": [], "heatmap": 9, "statist": 9, "develop": 0, "guid": 0, "applic": 2, "set": 2, "modul": [0, 6], "overview": 0, "build": 0, "instruct": 0, "debug": 0, "style": 0, "registr": 7, "process": [], "entranc": 0, "neural": 8, "network": 8, "gener": 0, "toolkit": 0, "librari": 0, "python": 0, "docstr": 0, "graph": 9}, "envversion": {"sphinx.domains.c": 3, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 9, "sphinx.domains.index": 1, "sphinx.domains.javascript": 3, "sphinx.domains.math": 2, "sphinx.domains.python": 4, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx": 60}, "alltitles": {"Modules": [[6, "modules"]], "Image Segmentation": [[8, "image-segmentation"]], "Thresholding": [[8, "thresholding"]], "Neural Network": [[8, "neural-network"]], "Developer Guide": [[0, "developer-guide"]], "Module Overview": [[0, "module-overview"]], "entrance": [[0, "entrance"]], "preprocess": [[0, "module-MRIphantom_desktop.src.preprocess.unpack"]], "segmentation": [[0, "module-MRIphantom_desktop.src.segmentation.process"]], "visualization": [[0, "module-MRIphantom_desktop.src.visualization.histogram"]], "Build Instructions": [[0, "build-instructions"]], "Debugging": [[0, "debugging"]], "Style Guide": [[0, "style-guide"]], "General": [[0, "general"]], "Toolkits and libraries": [[0, "toolkits-and-libraries"]], "Python": [[0, "python"]], "Docstrings": [[0, "docstrings"]], "Welcome to MRIphantom QA Solution\u2019s documentation!": [[1, "welcome-to-mriphantom-qa-solution-s-documentation"]], "Indices and tables": [[1, "indices-and-tables"]], "Application Settings": [[2, "application-settings"]], "Data Loading and Saving": [[3, "data-loading-and-saving"]], "Import data": [[3, "import-data"]], "Export data": [[3, "export-data"]], "Getting Started": [[4, "getting-started"]], "System requirements": [[4, "system-requirements"]], "Operating system versions": [[4, "operating-system-versions"]], "Hardware configuration": [[4, "hardware-configuration"]], "Installation from source": [[4, "installation-from-source"]], "Using MRIphantom QA Solution": [[4, "using-mriphantom-qa-solution"]], "Basics": [[4, "basics"]], "Image Preprocessing": [[5, "image-preprocessing"]], "Original resolution": [[5, "original-resolution"]], "Interpolation (better quality detection)": [[5, "interpolation-better-quality-detection"]], "Image Registration": [[7, "image-registration"]], "User Interface": [[9, "user-interface"]], "Main Window": [[9, "main-window"]], "Visualizations": [[9, "visualizations"]], "3D viewer": [[9, "d-viewer"]], "2D viewer": [[9, "id1"]], "Graphs": [[9, "graphs"]], "Heatmap": [[9, "heatmap"]], "Statistics Table": [[9, "statistics-table"]]}, "indexentries": {"histogram (class in mriphantom_desktop.src.visualization.histogram)": [[0, "MRIphantom_desktop.src.visualization.histogram.Histogram"]], "mriphantom_desktop.src.preprocess.unpack": [[0, "module-MRIphantom_desktop.src.preprocess.unpack"]], "mriphantom_desktop.src.segmentation.process": [[0, "module-MRIphantom_desktop.src.segmentation.process"]], "mriphantom_desktop.src.visualization.histogram": [[0, "module-MRIphantom_desktop.src.visualization.histogram"]], "mriphantom_desktop.src.visualization.plots": [[0, "module-MRIphantom_desktop.src.visualization.plots"]], "mriphantom_desktop.src.visualization.scatter2d": [[0, "module-MRIphantom_desktop.src.visualization.scatter2d"]], "mriphantom_desktop.src.visualization.scatter3d": [[0, "module-MRIphantom_desktop.src.visualization.scatter3d"]], "mriphantom_desktop.src.visualization.table": [[0, "module-MRIphantom_desktop.src.visualization.table"]], "mriphantom_desktop.src.visualization.viewer": [[0, "module-MRIphantom_desktop.src.visualization.viewer"]], "plots (class in mriphantom_desktop.src.visualization.plots)": [[0, "MRIphantom_desktop.src.visualization.plots.Plots"]], "scatter2d (class in mriphantom_desktop.src.visualization.scatter2d)": [[0, "MRIphantom_desktop.src.visualization.scatter2d.Scatter2D"]], "scatter3d (class in mriphantom_desktop.src.visualization.scatter3d)": [[0, "MRIphantom_desktop.src.visualization.scatter3d.Scatter3D"]], "table (class in mriphantom_desktop.src.visualization.table)": [[0, "MRIphantom_desktop.src.visualization.table.Table"]], "viewer (class in mriphantom_desktop.src.visualization.viewer)": [[0, "MRIphantom_desktop.src.visualization.viewer.Viewer"]], "count_difference() (in module mriphantom_desktop.src.segmentation.process)": [[0, "MRIphantom_desktop.src.segmentation.process.count_difference"]], "dicom_to_nifti() (in module mriphantom_desktop.src.preprocess.unpack)": [[0, "MRIphantom_desktop.src.preprocess.unpack.dicom_to_nifti"]], "get_coords() (in module mriphantom_desktop.src.segmentation.process)": [[0, "MRIphantom_desktop.src.segmentation.process.get_coords"]], "init_histogram() (mriphantom_desktop.src.visualization.histogram.histogram method)": [[0, "MRIphantom_desktop.src.visualization.histogram.Histogram.init_histogram"]], "init_plots() (mriphantom_desktop.src.visualization.plots.plots method)": [[0, "MRIphantom_desktop.src.visualization.plots.Plots.init_plots"]], "init_scatter2d() (mriphantom_desktop.src.visualization.scatter2d.scatter2d method)": [[0, "MRIphantom_desktop.src.visualization.scatter2d.Scatter2D.init_scatter2d"]], "init_scatter3d() (mriphantom_desktop.src.visualization.scatter3d.scatter3d method)": [[0, "MRIphantom_desktop.src.visualization.scatter3d.Scatter3D.init_scatter3d"]], "init_table() (mriphantom_desktop.src.visualization.table.table method)": [[0, "MRIphantom_desktop.src.visualization.table.Table.init_table"]], "isolate_markers() (in module mriphantom_desktop.src.segmentation.process)": [[0, "MRIphantom_desktop.src.segmentation.process.isolate_markers"]], "module": [[0, "module-MRIphantom_desktop.src.preprocess.unpack"], [0, "module-MRIphantom_desktop.src.segmentation.process"], [0, "module-MRIphantom_desktop.src.visualization.histogram"], [0, "module-MRIphantom_desktop.src.visualization.plots"], [0, "module-MRIphantom_desktop.src.visualization.scatter2d"], [0, "module-MRIphantom_desktop.src.visualization.scatter3d"], [0, "module-MRIphantom_desktop.src.visualization.table"], [0, "module-MRIphantom_desktop.src.visualization.viewer"]], "perform_thresholding() (in module mriphantom_desktop.src.segmentation.process)": [[0, "MRIphantom_desktop.src.segmentation.process.perform_thresholding"]], "slice_img_generator() (in module mriphantom_desktop.src.segmentation.process)": [[0, "MRIphantom_desktop.src.segmentation.process.slice_img_generator"]]}})