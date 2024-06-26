"""Sub-component module"""
import time
import tkinter as tk
from tkinter import ttk
from controller import Controller


class FilterBar(ttk.Frame):
    """Filter bar for users to filtered wanted graph in Data Exploration page."""
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.controller = controller
        self.start_year = tk.IntVar()
        self.end_year = tk.IntVar()
        self.entity1 = tk.StringVar()
        self.entity2 = tk.StringVar()
        self.unit = tk.StringVar()
        self.mode = tk.StringVar()
        self.graph = tk.StringVar()
        self.init_components()
        self.graph_state = self.all_features
        self.mode_state = self.standard

    def all_features(self):
        """
        State which all features in the filter bar are enable.
        For Line graph and Bar graph only.
        """
        self.en1_cbb.configure(state="readonly")
        self.en2_cbb.configure(state="readonly")
        self.yren_cbb.configure(state="readonly")
        self.mode_cbb.configure(state="readonly")
        self.mode.set("Standard")
        self.controller.generator.setup(mode="standard")
        self.controller.generator.set_all()

    def histogram(self):
        """
        State which some features in the filter bar are enable.
        For Histogram.
        """
        self.en1_cbb.configure(state="disabled")
        self.en2_cbb.configure(state="disabled")
        self.yren_cbb.configure(state="disabled")
        self.mode_cbb.configure(state="disabled")
        self.mode.set("Standard")
        self.controller.generator.setup(mode="standard")
        self.controller.generator.set_only_country()

    def standard(self):
        """
        State for Standard mode.
        For Standard mode only.
        """
        self.en1_cbb.configure(state="readonly")
        self.en2_cbb.configure(state="readonly")
        self.controller.generator.set_all()

    def top5(self):
        """
        State for Top rankings' mode.
        For Top rankings mode only.
        """
        self.en1_cbb.configure(state="disabled")
        self.en2_cbb.configure(state="disabled")
        self.controller.generator.set_only_country()

    def handle_mode_select(self, *args):
        """
        Switch mode state when users select mode.
        """
        if self.mode.get() == "Standard":
            self.mode_state = self.standard
            self.controller.generator.setup(mode='standard')
        elif self.mode.get() == "Top Rankings":
            self.mode_state = self.top5
            self.controller.generator.setup(mode='top5')
        self.mode_state()

    def handle_graph_select(self, *args):
        """
        Switch graph state when users select graph.
        """
        if self.graph.get() == 'Histogram':
            self.graph_state = self.histogram
        else:
            self.graph_state = self.all_features
        self.graph_state()
        self.controller.generator.setup(graph=self.graph.get())

    def handle_start_year_select(self, *args):
        """
        Set start year attribute for generator and
        disabled select previous year for end year when users select begin year.
        """
        year = self.start_year.get()
        self.controller.generator.setup(start_year=year)

        year_arr = list(map(str, range(year, 2020)))
        self.yren_cbb.configure(values=year_arr)
        if year > self.end_year.get():
            self.end_year.set(year)
            self.controller.generator.setup(end_year=year)

    def handle_end_year_select(self, *args):
        """
        Set end year attribute for generator when users select end year.
        """
        year = self.end_year.get()
        self.controller.generator.setup(end_year=year)

    def handle_entity1_select(self, *args):
        """
        Set entity1 attribute for generator when users select entity1.
        """
        entity = self.entity1.get()
        self.controller.generator.setup(entity1=entity)

    def handle_entity2_select(self, *args):
        """
        Set entity2 attribute for generator when users select entity2.
        """
        entity = self.entity2.get()
        self.controller.generator.setup(entity2=entity)

    def handle_unit_select(self, *args):
        """
        Set unit attribute for generator when users select unit.
        """
        unit_label = self.unit.get()
        to_unit = {'Death rate': 'death_rate', 'Total deaths': 'death_total'}
        unit = to_unit[unit_label]
        self.controller.generator.setup(unit=unit)

        self.handle_select_death_rate()

    def handle_select_death_rate(self, *args):
        """
        Change values in entity combobox in case of
        the selected entities have no population value.
        """
        unit_label = self.unit.get()
        g_array = self.type_sel.get_array()

        if unit_label == 'Death rate' and g_array != ['All']:
            pop_list = self.controller.get_entity_list('POPULATION')
            self.en1_cbb.configure(values=pop_list)
            self.en2_cbb.configure(values=pop_list)
            if self.entity1.get() not in pop_list:
                self.entity1.set('World')
                self.controller.generator.setup(entity1='World')
            if self.entity2.get() not in pop_list:
                self.entity2.set('Thailand')
                self.controller.generator.setup(entity1='Thailand')
        else:
            all_list = self.controller.get_entity_list()
            self.en1_cbb.configure(values=all_list)
            self.en2_cbb.configure(values=all_list)

    def handle_generate(self, *args):
        """
        When users press the generate button,
        setup attributes and let the page handle generate graph.
        """
        g_array = self.type_sel.get_array()
        if g_array == ['All']:
            to_unit = {'Death rate': 'death_rate', 'Total deaths': 'death_total'}
            unit = to_unit[self.unit.get()]
            g_array = [unit]

        self.controller.generator.setup(array=g_array)

        self.parent.handle_generate()

    def init_components(self):
        """
        Initialise the components and layout for the UI.
        """
        options = {'font': ('Arial', 21, 'bold')}
        n_font = {'font': ('Arial', 14)}
        s_font = {'font': ('Arial', 11)}
        sticky = {'sticky': tk.NSEW}
        color = {'fg': "Black", 'bg': 'white'}
        pad = {'padx': 5}
        pad2 = {'pady': 5}

        # label
        self.label = tk.Label(self, text='Filter Bar', anchor=tk.W, **options, **color)

        # year filter
        self.yr_label = tk.Label(self, text='Year', anchor=tk.W, **n_font, **color)
        self.yrbg_label = tk.Label(self, text='Begin:', anchor=tk.W, **s_font, **color)
        self.yren_label = tk.Label(self, text='End:', anchor=tk.W, **s_font, **color)

        year1_arr = list(map(str, range(1990, 2020)))
        self.yrbg_cbb = ttk.Combobox(self, textvariable=self.start_year,
                                     values=year1_arr, state='readonly')
        self.yrbg_cbb.bind('<<ComboboxSelected>>', self.handle_start_year_select)
        self.yrbg_cbb.set('1990')

        year2_arr = list(map(str, range(self.start_year.get(), 2020)))
        self.yren_cbb = ttk.Combobox(self, textvariable=self.end_year,
                                     values=year2_arr, state='readonly')
        self.yren_cbb.bind('<<ComboboxSelected>>', self.handle_end_year_select)
        self.yren_cbb.set('2019')

        # entity filter
        self.en_label = tk.Label(self, text='Entity', anchor=tk.W, **n_font, **color)
        self.en1_label = tk.Label(self, text='Entity 1:', anchor=tk.W, **s_font, **color)
        self.en2_label = tk.Label(self, text='Entity 2:', anchor=tk.W, **s_font, **color)

        en_arr = self.controller.get_entity_list('POPULATION')
        self.en1_cbb = ttk.Combobox(self, textvariable=self.entity1,
                                    values=en_arr, state='readonly', width=33)
        self.en1_cbb.bind('<<ComboboxSelected>>', self.handle_entity1_select)
        self.en1_cbb.set('World')

        self.en2_cbb = ttk.Combobox(self, textvariable=self.entity2,
                                    values=en_arr, state='readonly', width=33)
        self.en2_cbb.bind('<<ComboboxSelected>>', self.handle_entity2_select)
        self.en2_cbb.set('Thailand')

        # type selection
        self.type_sel = TypeSelection(self, self.controller)
        self.type_sel.bind('<Leave>', self.handle_select_death_rate)

        # unit
        unit_arr = ('Death rate', 'Total deaths')
        self.unit_label = tk.Label(self, text='Unit', **n_font, **color)
        self.unit_cbb = ttk.Combobox(self, textvariable=self.unit,
                                     values=unit_arr, state='readonly')
        self.unit_cbb.bind('<<ComboboxSelected>>', self.handle_unit_select)
        self.unit.set("Death rate")

        # mode
        mode_arr = ("Standard", "Top Rankings")
        self.mode_label = tk.Label(self, text='Mode', **n_font, **color)
        self.mode_cbb = ttk.Combobox(self, textvariable=self.mode,
                                     values=mode_arr, state='readonly')
        self.mode_cbb.bind('<<ComboboxSelected>>', self.handle_mode_select)
        self.mode.set("Standard")

        # graph
        graph_arr = ("Line Graph", "Bar Graph", "Histogram")
        self.grph_label = tk.Label(self, text='Graph', **n_font, **color)
        self.grph_cbb = ttk.Combobox(self, textvariable=self.graph,
                                     values=graph_arr, state='readonly')
        self.grph_cbb.bind('<<ComboboxSelected>>', self.handle_graph_select)
        self.graph.set("Line Graph")

        # generate button
        self.gen = tk.Button(self, text='GENERATE', **options, **color)
        self.gen.bind('<Button>', self.handle_generate)

        # grid
        self.label.grid(row=0, column=0, columnspan=4, **sticky)

        self.yr_label.grid(row=1, column=0, columnspan=2, **sticky, **pad)
        self.yrbg_label.grid(row=2, column=0, **sticky, **pad)
        self.yren_label.grid(row=2, column=1, **sticky, **pad)
        self.yrbg_cbb.grid(row=3, column=0, **sticky, **pad)
        self.yren_cbb.grid(row=3, column=1, **sticky, **pad)

        self.en_label.grid(row=1, column=2, columnspan=2, **sticky, **pad)
        self.en1_label.grid(row=2, column=2, **sticky, **pad)
        self.en2_label.grid(row=2, column=3, **sticky, **pad)
        self.en1_cbb.grid(row=3, column=2, **sticky, **pad)
        self.en2_cbb.grid(row=3, column=3, **sticky, **pad)

        self.type_sel.grid(row=4, column=0, columnspan=4, **sticky, **pad2)

        self.unit_label.grid(row=5, column=0, **sticky)
        self.unit_cbb.grid(row=5, column=1, **sticky, **pad2)

        self.mode_label.grid(row=6, column=0, **sticky)
        self.mode_cbb.grid(row=6, column=1, **sticky, **pad2)

        self.grph_label.grid(row=7, column=0, **sticky)
        self.grph_cbb.grid(row=7, column=1, **sticky, **pad2)

        self.gen.grid(row=9, column=0, columnspan=4, **sticky)

        for i in range(10):
            self.rowconfigure(i, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(8, weight=5)
        for i in range(4):
            self.columnconfigure(i, weight=1)

        style = ttk.Style()
        style.configure("My.TFrame", background='white')
        self.configure(style="My.TFrame", borderwidth=20)


class TypeSelection(ttk.Frame):
    """Type selection for users to select which subset of people
    they want to view which is a part of the filter bar.
    """
    def __init__(self, parent, controller: Controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.controller = controller
        self.checkbutton = []
        self.avail_age = ('Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years', 'All')
        self.avail_type = ('pedestrian', 'motor vehicle', 'motorcyclist', 'cyclist', 'other', 'All')
        self.age_list = ('age_0_4', 'age_5_14', 'age_15_49', 'age_50_69', 'age_70', 'All')
        self.type_list = ('type_pedestrian', 'type_motorvehicle', 'type_motorcyclist',
                          'type_cyclist', 'type_other', 'All')
        self.cur_list = self.avail_age
        self.cur_list_use = self.age_list
        self.type = tk.StringVar()
        self.sel1 = tk.IntVar()
        self.sel2 = tk.IntVar()
        self.sel3 = tk.IntVar()
        self.sel4 = tk.IntVar()
        self.sel5 = tk.IntVar()
        self.sel6 = tk.IntVar()
        self.sel_list = [self.sel1, self.sel2, self.sel3, self.sel4, self.sel5, self.sel6]
        self.init_components()

    def handle_select_all(self, *args):
        """
        Deselect other options when users select all options.
        """
        for ckb in self.checkbutton[:-1]:
            ckb.deselect()
        self.ckb6.select()

    def handle_combobox(self, *args):
        """
        Switch the label of the options according to the type users chose.
        """
        if self.type.get() == 'by age':
            self.cur_list = self.avail_age
            self.cur_list_use = self.age_list
        elif self.type.get() == 'by vehicle type':
            self.cur_list = self.avail_type
            self.cur_list_use = self.type_list
        for i in range(len(self.cur_list)):
            self.checkbutton[i].configure(text=self.cur_list[i])
        for ckb in self.checkbutton[:-1]:
            ckb.deselect()
        self.ckb6.select()

    def handle_select_normal(self, *args):
        """
        Deselect all option when users select other options.
        """
        self.ckb6.deselect()
        if not self.get_array():
            self.ckb6.select()

    def init_components(self):
        """
        Initialise the components and layout for the UI.
        """
        n_font = {'font': ('Arial', 14)}
        s_font = {'font': ('Arial', 11)}
        sticky = {'sticky': tk.NSEW}
        color = {'fg': "Black", 'bg': 'white'}
        pad = {'padx': 5}
        pad2 = {'pady': 5}

        # label
        self.label = tk.Label(self, text='Select type filter', **n_font, **color)

        # combobox
        type_arr = ('by age', 'by vehicle type')
        self.combobox = ttk.Combobox(self, textvariable=self.type,
                                     values=type_arr, state='readonly')
        self.combobox.bind('<<ComboboxSelected>>', self.handle_combobox)
        self.type.set('by age')

        # check buttons
        self.ckb1 = tk.Checkbutton(self)
        self.ckb2 = tk.Checkbutton(self)
        self.ckb3 = tk.Checkbutton(self)
        self.ckb4 = tk.Checkbutton(self)
        self.ckb5 = tk.Checkbutton(self)
        self.ckb6 = tk.Checkbutton(self)
        self.checkbutton = [self.ckb1, self.ckb2, self.ckb3, self.ckb4, self.ckb5, self.ckb6]
        for i in range(len(self.checkbutton)):
            self.checkbutton[i].configure(text=self.cur_list[i], variable=self.sel_list[i],
                                          onvalue=i, offvalue=-1, background='white', width=5,
                                          anchor=tk.W, command=self.handle_select_normal, **s_font)
        self.ckb6.configure(command=self.handle_select_all)

        # grid
        self.label.grid(row=0, column=0, columnspan=3, **sticky, **pad)

        self.combobox.grid(row=0, column=3, columnspan=3, **sticky, **pad2)

        for i in range(len(self.checkbutton)):
            self.checkbutton[i].grid(row=1, column=i+1, **sticky, **pad)

        for i in range(2):
            self.rowconfigure(i, weight=1)
        for i in range(6):
            self.columnconfigure(i, weight=1)

        style = ttk.Style()
        style.configure("My.TFrame", background='white')
        self.configure(style="My.TFrame", borderwidth=20)

        for ckb in self.checkbutton:
            ckb.deselect()
        self.ckb6.select()

    def get_array(self):
        """
        Return a list (array) according to which check buttons is chosen.

        :return: list, array attribute of the GraphGenerator
        """
        graph = self.controller.generator.graph
        sel_val = list(map(lambda x: x.get(), self.sel_list[:-1]))
        if -1 not in sel_val and graph != 'Bar Graph':
            return ['All']

        lst = []
        for sel in self.sel_list:
            if sel.get() > -1:
                lst.append(self.cur_list_use[sel.get()])
        return lst


class Keypad(ttk.Frame):
    """Keypad class which inherit from tkinter Frame"""
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        # keynames and columns
        self.keynames = keynames
        self.buttons = []
        self.init_components(columns)

    def init_components(self, columns):
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        options = {'font': ('Arial', 12)}
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 2, 'pady': 3}
        color = {'fg': "Black", 'bg': 'white'}

        for i in range(len(self.keynames)):
            num_button = tk.Button(self, text=self.keynames[i], **color, **options)
            row = i // columns
            col = i % columns
            num_button.grid(row=row, column=col, **pad, **sticky)
            self.buttons.append(num_button)

        for i in range(len(self.keynames) // columns):
            self.rowconfigure(i, weight=1)
        for i in range(columns):
            self.columnconfigure(i, weight=1)

    def bind(self, sequence, func, add=''):
        """Bind an event handler to an event sequence."""
        for button in self.buttons:
            button.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.buttons:
            button.configure({key: value})

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.buttons[0].config(key)[-1]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons."""
        for button in self.buttons:
            button.configure(cnf, **kwargs)
