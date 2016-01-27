from bokeh.plotting import figure, output_file, show, vplot

# ==============================================================================
#                                                                  PLOT SETTINGS
# ==============================================================================
BLUE = "#1A94D6"
ORANGE = "#FF8000"
GREEN = "#73AD21"

BLUE_PALE = "#A2C4DA"
ORANGE_PALE = "#F8C381"
GREEN_PALE = "#BBF864"

COLORS = [BLUE,  ORANGE, GREEN]
COLORS_PALE = [BLUE_PALE,  ORANGE_PALE, GREEN_PALE]



#===============================================================================
#                                                                PARAMETER PLOTS
#===============================================================================
def parameter_plots(x, results_dict, x_label, title_accuracy, title_time,
                    legend_pos="top_right"):
    """
    :param x: (list)
        The parameter values (used as the x axis)
    :param results_dict: (dict)
        The results dictionary returned by the looping parameters function
    :param x_label: (string)
        Label to use on the x axis
    :param title_accuracy: (string)
        Title For the Accuracy Plot
    :param title_time: (string)
        Title for the training time plot
    :param legend_pos: (string)
        Position of the legend
    """
    # =================
    # MAX DEPTH PLOTS
    # =================
    # --------------
    # ACCURACY PLOT
    # --------------
    s1 = figure(title=title_accuracy, width=600, height=400,
                x_axis_label=x_label,
                y_axis_label='Accuracy')
    s1.line(x, results_dict["in_sample_acc"],
            legend="In sample Accuracy", line_width=2, color=BLUE)
    s1.line(x, results_dict["out_sample_acc"],
            legend="Out of sample Accuracy", line_width=2, color=ORANGE)
    s1.legend.location = legend_pos
    s1.logo = None
    s1.toolbar_location = None

    # ---------------
    # TRAIN TIME PLOT
    # ---------------
    s2 = figure(title=title_time, width=600, height=400,
                x_axis_label=x_label,
                y_axis_label='Training Time (secs)')
    s2.line(x, results_dict["train_time"],
            line_width=2, color=ORANGE)
    s2.logo = None
    s2.toolbar_location = None

    # ----------------
    # VERTICALLY STACK
    # ----------------
    p = vplot(s1, s2)
    show(p)

