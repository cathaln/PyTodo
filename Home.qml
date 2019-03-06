import QtQuick 2.12
import QtQuick.Controls 2.5

Page {

    id: root
    title: qsTr("PyTodo")

    ScrollView {
        width: window.width * 0.9
        height: window.height * 0.9
        clip: true

        anchors.centerIn: parent

        Row {
            id: column_holder
            anchors.fill: parent

            Column {
                spacing: 5
                Repeater {
                    model: board_col1
                    delegate: Rectangle {
                        height: model.get_height
                        width: model.get_width
                        color: model.get_color
                    }
                }
            }

        }
    }

}
