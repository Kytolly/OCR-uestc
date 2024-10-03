#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "worker.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void onButtonClick(); // 按钮点击将路径发送到后台服务
    void onResultReady(const QString& result); // 接受后台返回处理结果准备展示

private:
    Ui::MainWindow *ui;
    TirP::Worker *worker;
};
#endif // MAINWINDOW_H
