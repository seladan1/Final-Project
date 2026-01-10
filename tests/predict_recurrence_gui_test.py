import sys
from unittest.mock import MagicMock, patch
import pandas as pd

#gui class uses gui_utils, messagebox,showinfo() - we dont need it so we'll use mockito to ignore it
sys.modules["gui_graphic_utils"] = MagicMock()
@patch("tkinter.messagebox.showinfo")
def test_predict_recurrence_probability(mock_showinfo):
    import src.predict_recurrence_gui as gui

    #generate data where treatment doesn't work 60% of times, we'll check if the function calculates correctly
    gui.df = pd.DataFrame({
        "Tumor Location": ["A", "A", "A", "A", "A"],
        "Tumor Grade": ["G1", "G1", "G1", "G1", "G1"],
        "Tumor Type": ["T1", "T1", "T1", "T1", "T1"],
        "Treatment": ["X", "X", "X", "X", "X"],
        "Recurrence": [1, 1, 0, 1, 0]
    })

    gui.features = ["Tumor Location", "Tumor Grade", "Tumor Type", "Treatment"] # all the diff features of df

    # our gui class uses .get().
    # we can't use it here, we'll use a dummy class to just copy the values from the df to the field get
    class SimpleVar:
        def __init__(self, value):
            self.value = value
        def get(self):
            return self.value

    gui.gui_vars = {
        "Tumor Location": SimpleVar("A"),
        "Tumor Grade": SimpleVar("G1"),
        "Tumor Type": SimpleVar("T1"),
        "Treatment": SimpleVar("X")
    }

    assert gui.predict_recurrence() == 60.0 #check if function works correctly