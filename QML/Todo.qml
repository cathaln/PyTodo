import QtQuick 2.12
import QtQuick.Controls 2.5

Page {

    id: root

    Column {

        spacing: 20
        anchors.horizontalCenter: parent.horizontalCenter
        padding: 50

        TextField {
            id: todo_header

            width: 200

            placeholderText: "Title"
        }

        ScrollView {
            width: window.width * 0.85
            height: window.height/2
            clip: true

            TextArea {
                id: todo_body
                font.pointSize: 14
                wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                placeholderText: "What has to be done?"
                text: ""
            }
        }
    }
}

/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
