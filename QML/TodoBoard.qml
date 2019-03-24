import QtQuick 2.12
import QtQuick.Controls 2.5

Page {

    id: root

    GridView {
        id: todo_board

        anchors.centerIn: parent
        width: window.width * 0.9
        height: window.height * 0.8

        cellHeight: 170
        cellWidth: 170

        delegate: Item {
            Column {
                Rectangle {
                    width: 150
                    height: 150
                    color: get_color
                    anchors.horizontalCenter: parent.horizontalCenter
                    radius: 5

                    Text {
                        text: get_text
                        anchors.centerIn: parent
                        font.bold: true
                        color: '#ffffff'
                    }
                }


            }
        }
        // set model which has been exported from python
        model: board_todo
    }
}



/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
