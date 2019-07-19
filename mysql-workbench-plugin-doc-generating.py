# -*- coding: utf-8 -*-
# MySQL Workbench Plugin
# Written in MySQL Workbench 6.3.10
#
# Original Author: Hieu Le
# Author: thefreelux <https://github.com/thefreelux>

from wb import *
import grt
import mforms

ModuleInfo = DefineModule("ModelDocumentation", author="Hieu Le", version="1.0.0", description="Génération de la documentation Markdown à partir d'un modèle EER.")

# This plugin takes no arguments
@ModuleInfo.plugin("info.hieule.wb.documentation", caption="Générer de la documentation (Markdown)", description="description", input=[wbinputs.currentDiagram()], pluginMenu="Utilities")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)
def documentation(diagram):

    text = "# Documentation de Schéma\n\n"
    text += "Documentation de modèle MySQL Workbench v1.0.0 \n\n"

    
    for figure in diagram.figures:
        if hasattr(figure, "table") and figure.table:
            text += writeTableDoc(figure.table)

    mforms.Utilities.set_clipboard_text(text)
    mforms.App.get().set_status_text("Documentation générée dans le presse-papier. Collez-le dans votre editeur.")

    print "La documentation est copiée dans le presse-papier."
    return 0

def writeTableDoc(table):
    text = "## Table `" + table.name + "`\n\n"

    text += "### Description \n\n"

    text += table.comment + "\n\n"

    text += "### Colonnes \n\n"

    text += "| Colonne | Type | Attributs | Défaut | Description |\n| --- | --- | --- | --- | ---  |\n"

    for column in table.columns:
        text += writeColumnDoc(column, table)

    text += "\n\n"

    if (len(table.indices)):
        text += "### Index \n\n"

        text += "| Nom | Colonne | Type |\n| --- | --- | --- |\n"

        for index in table.indices:
            text += writeIndexDoc(index)

    text += "\n\n"

    return text


def writeColumnDoc(column, table):
    # column name
    text = "| `" + column.name + "`"

    # column type name
    if column.simpleType:
        text += " | " + column.simpleType.name
        # column max lenght if any
        if column.length != -1:
            text += "(" + str(column.length) + ")"
    else:
        text += " | "

    

    text += " | "

    # column attributes
    attribs = [];

    isPrimary = False;
    isUnique = False;
    for index in table.indices:
        if index.indexType == "PRIMARY":
            for c in index.columns:
                if c.referencedColumn.name == column.name:
                    isPrimary = True
                    break
        if index.indexType == "UNIQUE":
            for c in index.columns:
                if c.referencedColumn.name == column.name:
                    isUnique = True
                    break

    # primary?
    if isPrimary:
        attribs.append("PRIMARY")

    # auto increment?
    if column.autoIncrement == 1:
        attribs.append("Auto increments")

    # not null?
    if column.isNotNull == 1:
        attribs.append("Not null")

    # unique?
    if isUnique:
        attribs.append("Unique")

    text += ", ".join(attribs)

    # column default value
    text += " | " + (("`" + column.defaultValue + "`") if column.defaultValue else " ")

    # column description
    text += " | " + (nl2br(column.comment) if column.comment else " ")

    # foreign key
    for fk in table.foreignKeys:
        if fk.columns[0].name == column.name:
            text +=  ("<br/><br/>" if column.comment else "") + "**clé étrangère** sur la colonne `" + fk.referencedColumns[0].name + "` sur la table `" + fk.referencedColumns[0].owner.name + "`."
            break


    # finish
    text  +=  " |" + "\n"
    return text

def writeIndexDoc(index):

    # index name
    text = "| " + index.name

    # index columns
    text += " | " + ", ".join(map(lambda x: "`" + x.referencedColumn.name + "`", index.columns))

    # index type
    text += " | " + index.indexType

    # index description
    text += " | " + (nl2br(index.comment) if index.comment else " ")

    # finish
    text += " |\n"

    return text

def nl2br(text):
    return "<br />".join(map(lambda x: x.strip(), text.split("\n")))
