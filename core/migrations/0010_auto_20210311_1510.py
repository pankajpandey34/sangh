# Generated by Django 3.1.5 on 2021-03-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210305_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.ImageField(upload_to='img')),
                ('linkto', models.CharField(choices=[('DrRangerSenerity', 'पदक्रम उपवनक्षेत्रपाल'), ('ForesterSenerity', 'पदक्रम वनपाल'), ('FgSenerity', 'पदक्रम वनरक्षक'), ('HardaSanghLetter', 'हरदा संघ के पत्र'), ('BhopalSanghLetter', 'भोपाल संघ के पत्र'), ('Gajat', 'राजपत्र'), ('Parpatra', 'प्रपत्र'), ('Niyam', 'नियम'), ('Act', 'अधिनियम'), ('empRule', 'सेवा भीर्ती नियम'), ('RtiAct', 'सूचना का अधिकार'), ('PccfLetter', 'प्रधान मुख्\u200dय वनसंरक्षक के पत्र'), ('CcfLetter', 'मुख्\u200dय वन संरक्षक के पत्र'), ('DfoLetter', 'वनमंडल के पत्र')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='range',
            name='subdivision',
        ),
        migrations.RemoveField(
            model_name='subdivision',
            name='division',
        ),
        migrations.AlterField(
            model_name='pdffile',
            name='file',
            field=models.FileField(upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='pdffile',
            name='linkto',
            field=models.CharField(choices=[('DrRangerSenerity', 'पदक्रम उपवनक्षेत्रपाल'), ('ForesterSenerity', 'पदक्रम वनपाल'), ('FgSenerity', 'पदक्रम वनरक्षक'), ('HardaSanghLetter', 'हरदा संघ के पत्र'), ('BhopalSanghLetter', 'भोपाल संघ के पत्र'), ('Gajat', 'राजपत्र'), ('Parpatra', 'प्रपत्र'), ('Niyam', 'नियम'), ('Act', 'अधिनियम'), ('empRule', 'सेवा भीर्ती नियम'), ('RtiAct', 'सूचना का अधिकार'), ('PccfLetter', 'प्रधान मुख्\u200dय वनसंरक्षक के पत्र'), ('CcfLetter', 'मुख्\u200dय वन संरक्षक के पत्र'), ('DfoLetter', 'वनमंडल के पत्र')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vetan5680',
            name='division',
            field=models.CharField(choices=[('hardaT', 'सामान्\u200dय वनमंडल हरदा'), ('hardaP', 'उत्\u200dपादन वनमंडल हरदा')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vetan5680',
            name='range',
            field=models.CharField(choices=[('makraiT', 'मकड़ाई सामान्\u200dय'), ('magardhaT', 'मगरधा सामान्\u200dय'), ('borpaniT', 'बोरपानी सामान्\u200dय'), ('handiaT', 'हंडिया सामान्\u200dय'), ('temagoanT', 'टेमागांव सामान्\u200dय'), ('rahatgoanT', 'रहटगांव सामान्\u200dय'), ('makraiP', 'मकड़ाई उत्\u200dपादन'), ('magardhaP', 'मगरधा उत्\u200dपादन'), ('borpaniP', 'बोरपानी उत्\u200dपादन'), ('handiaP', 'हंडिया उत्\u200dपादन'), ('temagoanP', 'टेमागांव उत्\u200dपादन'), ('rahatgoanP', 'रहटगांव उत्\u200dपादन')], max_length=100),
        ),
        migrations.DeleteModel(
            name='division',
        ),
        migrations.DeleteModel(
            name='pdffor',
        ),
        migrations.DeleteModel(
            name='range',
        ),
        migrations.DeleteModel(
            name='subdivision',
        ),
    ]