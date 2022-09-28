#include <QCoreApplication>
#include <iostream>
#include <QMap>
#include <QString>
#include <QDebug>


QString Simple_substitution_cipher(QString s, QString key = "XGUACDTBFHRSLMQVYZWIEJOKNP")
//Takes:
//      an input QString
//Returns:
//      encrypted with Simple substitution metod QString
{
    int len = s.size();
    QString encrypted(len);
    static QMap <char, QChar> map ;

    for (int i = 0; i < 26; i++)
    {
        map.insert('A'+i,key.at(i).toUpper());
        map.insert('a'+i,key.at(i).toLower());
    }

    QList<QChar> values = map.values();
    QList<char> keys = map.keys();

    for (int i = 0; i < s.size(); i++)
    {
        for (int j = 0; j < values.size(); j++)
        {
            if (s[i] == keys[j])
                encrypted[i] = values[j];
            s.remove(i);
        }
    }
    return encrypted;
}
QString Simple_substitution_decryption (QString s, QString key = "XGUACDTBFHRSLMQVYZWIEJOKNP")
//Takes:
//      encrypted with Simple substitution cipher QString
//Returns:
//      an original QString
{
        int len = s.size();
        QString decrypted(len);
        static QMap <char, QChar> map ;

        for (int i = 0; i < 26; i++)
        {
            map.insert('A'+i,key.at(i).toUpper());
            map.insert('a'+i,key.at(i).toLower());
        }

        QList<QChar> values = map.values();
        QList<char> keys = map.keys();

        for (int i = 0; i < s.size(); i++)
        {
            for (int j = 0; j < values.size(); j++)
            {
                if (s[i] == values[j])
                    decrypted[i] = keys[j];
                s.remove(i);
            }
        }
        return decrypted;
}

QString Caesar_cipher(QString s, int l)
//Takes:
//      an input QString
//Returns:
//      encrypted with Caesar cipher QString
{
    int len = s.size();
    QString encrypted(len);
    int str_ascii = 0;

    for (int i = 0; i < s.size(); i++)
    {
        str_ascii = s.at(i).toLatin1();

        if(s.at(i).isUpper())
        {
            encrypted[i] = (str_ascii + l - 'A') % 26 + 'A';
        }
        if(s.at(i).isLower())
        {
            encrypted[i] = (str_ascii + l - 'a') % 26 + 'a';
        }

    }
    return encrypted;
}

QString Caesar_decryption(QString s, int l)
//Takes:
//      encrypted with Caesar cipher QString
//Returns:
//      an original QString
{
    int len = s.size();
    QString decrypted(len);
    int str_ascii = 0;

    for (int i = 0; i < s.size(); i++)
    {
        str_ascii = s.at(i).toLatin1();

        if(s.at(i).isUpper())
        {
            decrypted[i] = (str_ascii + 26 - l - 'A') % 26 + 'A' ;
        }
        if(s.at(i).isLower())
        {
            decrypted[i] = (str_ascii + 26 - l - 'a') % 26 + 'a';
        }

    }
    return decrypted;
}

QString Transposition_cipher(QString s, int d = 23154)
//Takes:
//      an input QString
//      int param d - fixed order of symbols in resulting string
//Returns:
//      encrypted with Transition cipher QString
{

    QVector<int> key;
    QString encrypted(s.size());

    int number_of_digits = 0;

    while (!(d/10 == 0))
    {
       number_of_digits++;
       key.push_front(d%10);
       d/=10;
    }
       key.push_front(d%10);

    for (int i = 0; i < s.size(); i++)
    {
        encrypted[i] = s[key[i] - 1];
    }

    return encrypted;
}
QString Transposition_decryption(QString s, int d = 23154)
//Takes:
//      encrypted with Transposition cipher QString
//Returns:
//      an original QString
{
    QVector<int> key;
    QString decrypted(s.size());

    int number_of_digits = 0;

    while (!(d/10 == 0))
    {
       number_of_digits++;
       key.push_front(d%10);
       d/=10;
    }
       key.push_front(d%10);

    for (int i = 0; i < s.size(); i++)
    {
        decrypted[key[i] - 1] = s[i];
    }

    return decrypted;
}
QString Vigenere_cipher(QString str, QString key)
//Takes:
//      an input QString
//      int param d - fixed order of symbols in resulting string
//Returns:
//      encrypted with Vigenere cipher QString
{
    int len = str.size();
    QString encrypted(len);
    int key_ascii = 0, str_ascii = 0;
    int i = 0;

    while (key.size() < str.size())
    {
        key.push_back(key[i]);
        i++;
    }

    for (int i = 0; i < str.size(); i++)
    {
        if(str.at(i).isUpper())
        {
            key_ascii = key.at(i).toUpper().toLatin1();
            str_ascii = str.at(i).toUpper().toLatin1();
            encrypted[i] = (key_ascii + str_ascii) % 26 + 65;
        }
        if(str.at(i).isLower())
        {
            key_ascii = key.at(i).toLower().toLatin1();
            str_ascii = str.at(i).toLower().toLatin1();
            encrypted[i] = (key_ascii + str_ascii) % 26 + 65;
        }


    }
    return encrypted;
}

QString Vigenere_decryption(QString str, QString key)
//Takes:
//      encrypted with Vigenere cipher QString
//Returns:
//      an original QString
{

    int len = str.size();
    QString decrypted(len);
    int key_ascii = 0, str_ascii = 0;
    int i = 0;

    while (key.size() < str.size())
    {
        key.push_back(key[i]);
        i++;
    }

    for (int i = 0; i < str.size(); i++)
    {
        if(str.at(i).isUpper())
        {
            key_ascii = key.at(i).toUpper().toLatin1();
            str_ascii = str.at(i).toUpper().toLatin1();
            decrypted[i] = (str_ascii - key_ascii + 26) % 26 + 65;
        }
        if(str.at(i).isLower())
        {
            key_ascii = key.at(i).toLower().toLatin1();
            str_ascii = str.at(i).toLower().toLatin1();
            decrypted[i] = (str_ascii - key_ascii + 26) % 26 + 65;
        }

    }
    return decrypted;
}




int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QString s1{"Olenka"};
    QString s2{"OLENKA"};

    qDebug()<<"The input string is:"<<s1<<endl;

    qDebug()<<"Simple substitution cipher"<<Simple_substitution_cipher(s1);
    qDebug()<<"Simple substitution decryption"<<Simple_substitution_decryption(Simple_substitution_cipher(s1));

    qDebug()<<"Caesar cipher"<<Caesar_cipher(s1, 1);
    qDebug()<<"Caesar decryption"<<Caesar_decryption(Caesar_cipher(s1, 1), 1);

    qDebug()<<"Vigenere cipher"<<Vigenere_cipher(s2, "GAH");
    qDebug()<<"Vigenere decryption"<<Vigenere_decryption(Vigenere_cipher(s2, "GAH"), "GAH");

    qDebug()<<"Transposition cipher"<<Transposition_cipher(s1,231564);
    qDebug()<<"Transposition decryption"<<Transposition_decryption(Transposition_cipher(s1,231564),231564);

    return a.exec();
}

