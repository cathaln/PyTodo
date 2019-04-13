import QtQuick 2.12
import QtQuick.Controls 2.5
import 'Widgets'

Page {

    id: root

    property string todo_name
    property string todo_desc

    Column {

        spacing: 20
        anchors.horizontalCenter: parent.horizontalCenter
        padding: 50

        Row {
            spacing: 20

            TextField {
                id: todo_header
                width: 200
                placeholderText: "Title"
                color: 'orange'
                text: todo_name
            }
        }

        ScrollView {
            id: todo_scroll
            width: window.width * 0.85
            height: window.height/2
            clip: true

            TextArea {
                id: todo_body
                font.pointSize: 14
                wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                placeholderText: "What has to be done?"
                text: todo_desc
            }
        }

        PrimaryButton {
            id: save_todo
            anchors.right: todo_scroll.right
            setText: "\u2713"
            setWidth: 40
            setFontSize: 20

            onClicked: {

                board_todo.update_todo(todo_header.text, todo_body.text)
                stackView.pop()

            }

        }
    }
}

/*##^## Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
 ##^##*/
