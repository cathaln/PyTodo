import QtQuick 2.12
import QtQuick.Controls 2.5

Button {

    id: root
    height: 40
    width: 200

    property alias setText: root_text.text
    property alias setWidth: root.width
    property alias setFontSize: root_text.font.pointSize

    background: Rectangle {

        anchors.fill: parent
        radius: 5
        color: 'orange'

        Text {
            id: root_text
            text: ""
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            font.pointSize: 12
            color: 'white'
        }

    }
}
