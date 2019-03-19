import QtQuick 2.12
import QtQuick.Controls 2.5

Rectangle {

    id: root
    height: 40
    width: 200
    radius: 5
    color: 'lightblue'

    property alias setText: root_text.text

    Text {
        id: root_text
        text: ""
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        font.pointSize: 12
        color: 'white'
    }
}
