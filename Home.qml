import QtQuick 2.12
import QtQuick.Controls 2.5
import "Widgets"

Page {

    /*
    Fix so entire board sits in centre of screen (currently has a horizontal scroll).
    */

    id: root
    title: qsTr("PyTodo")

    Column {
        id: column
        spacing: 60

        anchors.centerIn: parent

        Text {
            id: tmp
            text: "PyTodo"
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 35
            color: 'lightblue'
        }

        Column {

            spacing: 15

            PrimaryButton{

                anchors.horizontalCenter: parent.horizontalCenter
                setText: "New Board"
            }

            PrimaryButton{

                anchors.horizontalCenter: parent.horizontalCenter
                setText: "Old Board"
            }
        }

    }

}





















/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
