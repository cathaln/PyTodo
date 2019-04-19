import QtQuick 2.12
import QtQuick.Controls 2.5

Page {

    id: root

    GridView {
        id: todo_board

        anchors.centerIn: parent
        width: window.width * 0.8
        height: window.height * 0.8

        cellHeight: 160
        cellWidth: 160

        delegate: Item {
            Column {
                Rectangle {
                    width: 150
                    height: 150
                    color: get_color
                    anchors.horizontalCenter: parent.horizontalCenter
                    radius: 5

                    Text {
                        text: get_name
                        anchors.centerIn: parent
                        font.bold: true
                        color: '#ffffff'
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: stackView.push('Todo.qml', {"todo_name": get_name, "todo_desc": get_description})

                    }
                }
            }
        }
        // set model which has been exported from python
        model: board_todo
    }

    Button {
        id: add_todo_button

        height: 50
        width: 50

        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 25

        background: Rectangle{

            color: "white"
            border.color: "orange"
            anchors.fill: parent
            radius: 50

            Text {
                id: add_plus
                text: "+"
                color: "orange"
                font.pointSize: 40

                anchors.centerIn: parent
                anchors.verticalCenterOffset: -2

            }
        }

        onClicked: {

            onClicked: stackView.push('Todo.qml', {"todo_name": "", "todo_desc": ""})

        }
    }

    /*Column {

        anchors.left: parent.left
        anchors.top: todo_board.top

        width: window.width * 0.1
        height: parent.height

        Button {
            id: add_todo_button

            height: parent.height
            width: parent.width

            background: Rectangle{

                color: "white"
                anchors.fill: parent

                Text {
                    id: add_plus
                    text: "+"
                    color: hovered ? "orange" : "white"
                    font.pointSize: 40

                    anchors.centerIn: parent
                    anchors.verticalCenterOffset: -20

                }
            }

            onClicked: {

                onClicked: stackView.push('Todo.qml', {"todo_name": "", "todo_desc": ""})

            }
        }*/

        /*Button {
            id: add_todo_button
            width: 50
            height: 50

            anchors.horizontalCenter: parent.horizontalCenter
            background: Rectangle{
                color: "orange"
                radius: 5
                Text {
                    id: plus_symbol
                    text: qsTr("+")
                    font.pointSize: 20
                    color: "white"
                    anchors.centerIn: parent
                    anchors.verticalCenterOffset: -2
                }
            }
        }

    }*/
}



/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
