from PyQt5 import QtCore, QtGui, QtWidgets

class UiHelpers:

    central_widget = None       # static main window widget

    def __init__(self):
        self.translate = QtCore.QCoreApplication.translate

    def add_tab(self, object_name, name, table_widget): # NOTE: this has been implermented into UI_tabs.
        """ Adds new tab to table widget

        :param object_name:     name of the object (should be unique to app)
        :param name:            name to display on tab
        :param table_widget:    table to add tab to
        :return:                the new tab
        """


        tab = QtWidgets.QWidget()
        tab.setObjectName( object_name )
        table_widget.addTab(tab, "")
        table_widget.setTabText(table_widget.indexOf(tab), self.translate("MainWindow", name))

        return tab

    def create_table_widget(self, parent_obj, obj_name, pos_rect):
        """ Creates new table widget

        :param parent_obj:  Parent object that will contain the table. (may be None)
        :param obj_name:    name of the object (should be unique to app)
        :param pos_rect:    position rect Tuple (x_pos, y_pos, width, height)
        :return:            the new table.
        """
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        table = QtWidgets.QTableWidget( parent_obj )
        table.setGeometry( QtCore.QRect( pos_rect[0], pos_rect[1], pos_rect[2], pos_rect[3] ) )
        table.setSizePolicy( size_policy )
        table.setObjectName( obj_name )

        return table

    def set_table_columns(self, table_widget, column_names):
        """ Sets columns for table

        :param table_widget:    table to set columns in
        :param column_names:    List of columns
        :return:                None
        """

        table_widget.setColumnCount( len(column_names) )

        for i in range( len( column_names ) ):
            item = QtWidgets.QTableWidgetItem()
            item.setText( self.translate("MainWindow", column_names[i] ) )
            table_widget.setHorizontalHeaderItem(i, item)

    def add_table_column(self, table_widget, column_id, label, row_data):

        table_widget.insertColumn(column_id)
        item = QtWidgets.QTableWidgetItem()
        item.setText(self.translate("MainWindow", label))
        table_widget.setHorizontalHeaderItem(column_id, item)

        for row in range( len(row_data) ):
            item = QtWidgets.QTableWidgetItem(row_data[row])
            table_widget.setItem( row, column_id, item )


    def get_cell_flags(self, editable):
        """Gets the cell flags"""
        flags = QtCore.Qt.ItemIsSelectable

        if editable:
            flags = flags | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

        return flags

    def set_table_rows(self, table, data, column_params):
        """ Set rows in table

        :param table:          table to set rows in
        :param data:           data to set in table, List[row][column]
        :param column_params:  list of tuples of params for column. (editable, type)
        :return:               None
        """
        column_names = [*column_params]  # get out keys are a list
        table.setRowCount( len(data) )

        # add our rows of columns
        for row in range(len(data)):
            for col in range(len(data[row])):
                # replace None with no text :)
                if data[row][col] is None:
                    data[row][col] = ""

                item = QtWidgets.QTableWidgetItem( str(data[row][col]) )
                item.setFlags( self.get_cell_flags( column_params[column_names[col]][0] ) )

                table.setItem( row, col, item )

    def add_table_row(self, table, data, row = -1, label=None, row_height=-1):
        """Add row at position

        :param table:   Table to add row to
        :param data:    row data List[column]
        :param row:     row to add data, -1 = add to end
        :return:        None
        """

        if row < 0 or row >= table.rowCount():
            row = table.rowCount()

        table.insertRow(row)

        if label is not None:
            item = QtWidgets.QTableWidgetItem()
            item.setText(self.translate("MainWindow", label))
            table.setVerticalHeaderItem(row, item)

        if row_height > 1:
            table.setRowHeight(row, row_height)

        for col in range( len(data) ):
            item = QtWidgets.QTableWidgetItem(data[col])
            table.setItem( row, col, item )

    def add_tree_item(self, parent, str):
        """ add item to tree

        :param parent:  tree item to add to
        :param str:     item display text
        :return:        QTreeWidgetItem
        """

        return QtWidgets.QTreeWidgetItem(parent, [str])

    def create_combo_box(self, values, id):
        """ Creates a combo box filled with values

        :param values:  List of values
        :param id:      Id of combo box
        :return:        combo box
        """
        comboBox = QtWidgets.QComboBox()
        comboBox.setGeometry(QtCore.QRect(100, 20, 191, 22))
        comboBox.setObjectName("comboBox_"+str(id))

        for v in values:
            comboBox.addItem(v)

        return comboBox

    def create_button(self, label, obj_name, position, pressed_signal=None):

        button = QtWidgets.QPushButton(label)
        button.setObjectName(obj_name)
        #button.setText( self.translate("MainWindow", label) )
        button.setGeometry(position[0], position[1], position[2], position[3])


        if pressed_signal is not None:
            button.clicked.connect(pressed_signal)

        return button
