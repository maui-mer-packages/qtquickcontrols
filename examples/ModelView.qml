import QtQuick 1.0
import "../components"
import "../components/plugin"

Item {
    id: root
    width: 600
    height: 300

    ListModel {
        id: listModel
        ListElement{ property: "title" ; caption: "Title" ; width: 100}
        ListElement{ property: "imagesource" ; caption: "Image Source" ; width: 200}
        ListElement{ property: "filename" ; caption: "File Name" ; width: 200}
    }
    XmlListModel {
        id: flickerModel
        source: "http://api.flickr.com/services/feeds/photos_public.gne?format=rss2&tags=" + "Qt"
        query: "/rss/channel/item"
        namespaceDeclarations: "declare namespace media=\"http://search.yahoo.com/mrss/\";"
        XmlRole { name: "title"; query: "title/string()" }
        XmlRole { name: "imagesource"; query: "media:thumbnail/@url/string()" }
        XmlRole { name: "filename"; query: "link/string()" }
    }

    Column {
        anchors.margins: 4
        spacing: 8

        TableView{
            headermodel: listModel
            model: flickerModel
            width: root.width
            height: root.height/2
        }

        TableView{
            headermodel: listModel
            model: flickerModel
            width: root.width
            height: root.height/2 - 10

            rowDelegate: Rectangle {
                color: itemselected ? "#888" : (alternaterow ? "#ccc" : "#ddd")
                clip: true
                Rectangle{
                    width: parent.width
                    height:1
                    anchors.bottom: parent.bottom
                    color: "#aaa"
                }
            }

            itemDelegate: Item {
                width: itemwidth
                height: itemheight
                clip: true
                Text {
                    anchors.fill: parent
                    anchors.leftMargin: 5
                    elide: Qt.ElideRight
                    text: itemvalue
                    color: itemselected ? "white" : "black"
                }
                Rectangle {
                    width: 1
                    height: parent.height
                    color: "#aaa"
                }
            }

            headerDelegate: Rectangle {
                color: "#555"
                Rectangle {
                    width: 1
                    height: parent.height
                    color: "#444"
                }
                Text {
                    text: itemvalue
                    anchors.centerIn:parent
                    color:"#ccc"
                }
            }
        }
    }
}