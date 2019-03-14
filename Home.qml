import QtQuick 2.12
import QtQuick.Controls 2.5

Page {

    /*
    Fix so entire board sits in centre of screen (currently has a horizontal scroll).
    */

    id: root
    title: qsTr("PyTodo")

    ScrollView {
        id: scrollview
        width: window.width * 0.85
        height: window.height * 0.8
        clip: true

        anchors.centerIn: parent

        Row {
            id: column_holder
            anchors.fill: parent
            spacing: 10

            // to do column
            Column {
                width: scrollview.width * 0.33
                spacing: 5
                Text {
                    id: todo_col_header
                    text: "To do"
                    padding: 10
                    anchors.horizontalCenter: parent.horizontalCenter

                    color: 'lightgrey'
                }
                Repeater {
                    model: board_col_todo
                    delegate: Rectangle {
                        height: 80
                        width: parent.width
                        color: model.get_color

                        Text {
                            id: todo_text
                            text: model.get_text

                            anchors.centerIn: parent
                        }
                    }
                }
            }

            // to work on column
            Column {
                width: scrollview.width * 0.33
                spacing: 5
                Text {
                    id: towork_col_header
                    text: "To work on"
                    padding: 10
                    anchors.horizontalCenter: parent.horizontalCenter

                    color: 'lightgrey'
                }
                Repeater {
                    model: board_col_towork
                    delegate: Rectangle {
                        height: 80
                        width: parent.width
                        color: model.get_color

                        Text {
                            id: towork_text
                            text: model.get_text

                            anchors.centerIn: parent
                        }
                    }
                }
            }

            // done column
            Column {
                width: scrollview.width * 0.33
                spacing: 5
                Text {
                    id: done_col_header
                    text: "Done"
                    padding: 10
                    anchors.horizontalCenter: parent.horizontalCenter

                    color: 'lightgrey'
                }
                Repeater {
                    model: board_col_done
                    delegate: Rectangle {
                        height: 80
                        width: parent.width
                        color: model.get_color

                        Text {
                            id: done_text
                            text: model.get_text

                            anchors.centerIn: parent
                        }
                    }
                }
            }

        }
    }

}
