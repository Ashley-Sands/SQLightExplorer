from PyQt5 import QtCore, QtGui, QtWidgets

class UiHelpers:

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

    def set_table_rows(self, table, data):
        """ Set rows in table

        :param table:   table to set rows in
        :param data:    data to set in table, List[row][column]
        :return:        None
        """

        table.setRowCount( len(data) )
        # add our rows of columns
        for row in range(len(data)):
            for col in range(len(data[row])):
                item = QtWidgets.QTableWidgetItem( data[row][col] )
                table.setItem( row, col, item )

    def add_table_row(self, table, data, row = -1):
        """Add row at position

        :param table:   Table to add row to
        :param data:    row data List[column]
        :param row:     row to add data, -1 = add to end
        :return:        None
        """

        if row < 0 or row >= table.rowCount():
            row = table.rowCount()

        table.insertRow(row)

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

