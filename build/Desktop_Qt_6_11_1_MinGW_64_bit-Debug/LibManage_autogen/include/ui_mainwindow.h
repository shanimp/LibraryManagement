/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QWidget *widgetMain;
    QLabel *lblpwd;
    QLabel *lbluser;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QPushButton *btnlogin;
    QPushButton *pushButton;
    QWidget *widgetIcon;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(748, 442);
        MainWindow->setMaximumSize(QSize(16777, 16777));
        MainWindow->setStyleSheet(QString::fromUtf8("QMainWindow {\n"
"    border-image: url(D:/first/LibManage/img/background.jpg);\n"
"}"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        QSizePolicy sizePolicy(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy);
        centralwidget->setMaximumSize(QSize(16777200, 16777200));
        centralwidget->setStyleSheet(QString::fromUtf8(""));
        widgetMain = new QWidget(centralwidget);
        widgetMain->setObjectName("widgetMain");
        widgetMain->setGeometry(QRect(450, 60, 261, 281));
        widgetMain->setAutoFillBackground(false);
        widgetMain->setStyleSheet(QString::fromUtf8("#widgetMain {\n"
"    background-color: #91c2a3;\n"
"}"));
        lblpwd = new QLabel(widgetMain);
        lblpwd->setObjectName("lblpwd");
        lblpwd->setGeometry(QRect(10, 110, 91, 41));
        QFont font;
        font.setFamilies({QString::fromUtf8("Calibri")});
        font.setPointSize(16);
        font.setBold(true);
        lblpwd->setFont(font);
        lbluser = new QLabel(widgetMain);
        lbluser->setObjectName("lbluser");
        lbluser->setGeometry(QRect(10, 70, 91, 31));
        lbluser->setFont(font);
        lbluser->setStyleSheet(QString::fromUtf8(""));
        lineEdit = new QLineEdit(widgetMain);
        lineEdit->setObjectName("lineEdit");
        lineEdit->setGeometry(QRect(110, 70, 141, 31));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Calibri")});
        font1.setPointSize(12);
        lineEdit->setFont(font1);
        lineEdit_2 = new QLineEdit(widgetMain);
        lineEdit_2->setObjectName("lineEdit_2");
        lineEdit_2->setGeometry(QRect(110, 120, 141, 31));
        lineEdit_2->setFont(font1);
        lineEdit_2->setEchoMode(QLineEdit::EchoMode::Password);
        btnlogin = new QPushButton(widgetMain);
        btnlogin->setObjectName("btnlogin");
        btnlogin->setGeometry(QRect(180, 170, 61, 31));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Calibri")});
        font2.setPointSize(12);
        font2.setBold(true);
        btnlogin->setFont(font2);
        btnlogin->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #22C55E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #91e3af;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b4c2b9;\n"
"}"));
        pushButton = new QPushButton(widgetMain);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(180, 250, 61, 21));
        QFont font3;
        font3.setFamilies({QString::fromUtf8("Calibri")});
        font3.setPointSize(11);
        font3.setBold(true);
        pushButton->setFont(font3);
        pushButton->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #22C55E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #91e3af;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b4c2b9;\n"
"}"));
        widgetIcon = new QWidget(centralwidget);
        widgetIcon->setObjectName("widgetIcon");
        widgetIcon->setGeometry(QRect(160, 40, 51, 51));
        widgetIcon->setStyleSheet(QString::fromUtf8("QWidget{\n"
"    border-image: url(D:/first/LibManage/img/bookIcon.jpg);\n"
"}\n"
""));
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(110, 100, 161, 71));
        QFont font4;
        font4.setFamilies({QString::fromUtf8("Calibri")});
        font4.setPointSize(36);
        font4.setBold(true);
        label->setFont(font4);
        label->setAutoFillBackground(false);
        label->setStyleSheet(QString::fromUtf8("color: rgb(0, 24, 0);\n"
"\n"
"\n"
""));
        label->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(50, 160, 291, 81));
        label_2->setFont(font4);
        label_2->setAutoFillBackground(false);
        label_2->setStyleSheet(QString::fromUtf8("\n"
"color: rgb(0, 24, 0);"));
        label_2->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(100, 240, 171, 71));
        label_3->setFont(font4);
        label_3->setStyleSheet(QString::fromUtf8("\n"
"color: rgb(0, 24, 0);"));
        label_3->setAlignment(Qt::AlignmentFlag::AlignCenter);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 748, 21));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        lblpwd->setText(QCoreApplication::translate("MainWindow", "password", nullptr));
        lbluser->setText(QCoreApplication::translate("MainWindow", "username", nullptr));
        lineEdit_2->setPlaceholderText(QString());
        btnlogin->setText(QCoreApplication::translate("MainWindow", "login", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", "Sign up", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Library", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Management", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "System", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
