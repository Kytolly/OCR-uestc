#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    , worker(new TirP::Worker)
{
    ui->setupUi(this);
    worker->start();

    connect(ui->pushButton, &QPushButton::clicked, this, &MainWindow::onButtonClick);

    connect(worker, &TirP::Worker::resultReady, this, &MainWindow::onResultReady);
    connect(worker, &TirP::Worker::error, this, [this](const QString &err){
        ui->textBrowser->setPlainText("Error: "+ err);
    });
}

MainWindow::~MainWindow()
{
    worker->stop();
    worker->wait();
    delete ui;
}

void MainWindow::onButtonClick(){
    QString inputText = ui->lineEdit->text();
    // qDebug()<<"get Text:"<<inputText;
    worker->sendMessage(inputText);
}

void MainWindow::onResultReady(const QString& result){
    ui->textBrowser->setPlainText(result);
}
