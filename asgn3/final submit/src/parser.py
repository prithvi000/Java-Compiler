#!/usr/bin/python
import ply.lex as lex
import sys
import ply.yacc as yacc
from lexer import tokens
import logging
# print tokens
nonterminals=[]
output=[]
countg = 0
revoutput=[]
finalout=[]
# def p_program(p):
#     '''program : Importstatements '''



def p_CompilationUnit(p):
    '''CompilationUnit : ProgramFile
    '''
    revoutput.append(p.slice)

def p_ProgramFile(p):
    ''' ProgramFile : Importstatements TypeDeclarationOptSemi
                | Importstatements
                | TypeDeclarationOptSemi
    '''
    revoutput.append(p.slice)

def p_Importstatements(p):
    '''Importstatements : Importstatement
                    | Importstatements Importstatement
    '''
    revoutput.append(p.slice)
def p_Importstatement(p):
    '''Importstatement : KEYIMPORT QualifiedName Semicolons
                    | KEYIMPORT QualifiedName SEPDOT OPMULTIPLY Semicolons
    '''
    revoutput.append(p.slice)

def p_QualifiedName(p):
    '''QualifiedName : Identifier
                | QualifiedName SEPDOT Identifier
    '''
    revoutput.append(p.slice)

def p_Semicolons(p):
    '''Semicolons : SEPSEMICOLON
                | Semicolons SEPSEMICOLON 
    '''
    revoutput.append(p.slice)
def p_TypeSpecifier(p):
    '''TypeSpecifier : TypeName 
            | TypeName Dims              
    '''
    revoutput.append(p.slice)
#don't know what is Dims
def p_TypeName(p):
    '''TypeName : PrimitiveType
            | QualifiedName
    '''
    revoutput.append(p.slice)
def p_PrimitiveType(p):
    '''PrimitiveType : KEYBOOLEAN
                | KEYCHAR
                | KEYDOUBLE
                | KEYBYTE
                | KEYSHORT
                | KEYINT
                | KEYLONG
                | KEYVOID
                | KEYFLOAT
    '''
    revoutput.append(p.slice)
def p_ClassNameList(p):
    '''ClassNameList : QualifiedName
                 | ClassNameList SEPCOMMA QualifiedName
    '''
    revoutput.append(p.slice)

def p_TypeDeclarationOptSemi(p):
    '''TypeDeclarationOptSemi : TypeDeclaration
                    | TypeDeclaration Semicolons
    '''
    revoutput.append(p.slice)
def p_TypeDeclaration(p):
    '''TypeDeclaration : ClassHeader SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
                    | ClassHeader SEPLEFTPARAN SEPRIGHTPARAN
    '''
    revoutput.append(p.slice)
def p_ClassHeader(p):
    '''ClassHeader : Modifiers ClassWord Identifier
                | ClassWord Identifier
    '''
    revoutput.append(p.slice)
def p_ClassWord(p):
    '''ClassWord : KEYCLASS'''
    revoutput.append(p.slice)
def p_FieldDeclarations(p):
    '''FieldDeclarations : FieldDeclarationOptSemi
                    | FieldDeclarations FieldDeclarationOptSemi
    '''
    revoutput.append(p.slice)
def p_FieldDeclarationOptSemi(p):
    '''FieldDeclarationOptSemi : FieldDeclaration
                               | FieldDeclaration Semicolons
    '''
    revoutput.append(p.slice)
def p_FieldDeclaration(p):
    '''FieldDeclaration : FieldVariableDeclaration SEPSEMICOLON
                        | MethodDeclaration
                        | ConstructorDeclaration
                        | StaticInitializer
                        | NonStaticInitializer
                        | TypeDeclaration 
    '''
    revoutput.append(p.slice)
def p_FieldVariableDeclaration(p):
    '''FieldVariableDeclaration : Modifiers TypeSpecifier VariableDeclarators
                                | TypeSpecifier VariableDeclarators
    '''
    revoutput.append(p.slice)
def p_VariableDeclarators(p):
    '''VariableDeclarators : VariableDeclarator
                            | VariableDeclarators SEPCOMMA VariableDeclarator
    '''
    revoutput.append(p.slice)
def p_VariableDeclarator(p):
    ''' VariableDeclarator : DeclaratorName
                            | DeclaratorName OPEQUAL VariableInitializer
    '''
    revoutput.append(p.slice)

def p_VariableInitializer(p):
    '''VariableInitializer : Expression
                            | SEPLEFTPARAN SEPRIGHTPARAN
                            | SEPLEFTPARAN ArrayInitializers SEPRIGHTPARAN
    '''
    revoutput.append(p.slice)
def p_ArrayInitializers(p):
    '''ArrayInitializers : VariableInitializer
                            | ArrayInitializers SEPCOMMA VariableInitializer
                            | ArrayInitializers SEPCOMMA
    '''
    revoutput.append(p.slice)
def p_MethodDeclaration(p):
    '''MethodDeclaration : Modifiers TypeSpecifier MethodDeclarator MethodBody
                        | Modifiers TypeSpecifier MethodDeclarator Throws MethodBody
                        | TypeSpecifier MethodDeclarator Throws MethodBody
                        | TypeSpecifier MethodDeclarator MethodBody
    '''
    revoutput.append(p.slice)
def p_Throws(p):
    '''Throws : KEYTHROWS ClassNameList
    '''
    revoutput.append(p.slice)
def p_MethodDeclarator(p):
    '''MethodDeclarator : DeclaratorName SEPLEFTBRACE ParameterList SEPRIGHTBRACE
                    | DeclaratorName SEPLEFTBRACE SEPRIGHTBRACE
                    | MethodDeclarator OP_DIM
    '''
    revoutput.append(p.slice)
def p_ParameterList(p):
    '''ParameterList : Parameter
                    | ParameterList SEPCOMMA Parameter
    '''
    revoutput.append(p.slice)
def p_Parameter(p):
    '''Parameter : TypeSpecifier DeclaratorName
       '''
    revoutput.append(p.slice)
def p_DeclaratorName(p):
    '''DeclaratorName : Identifier
                    | DeclaratorName OP_DIM
    '''
    revoutput.append(p.slice)
# def p_Throws(p):
#     '''Throws : THROWS ClassNameList'''

def p_MethodBody(p):
    '''MethodBody : Block
                | SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_ConstructorDeclaration(p):
    '''ConstructorDeclaration : Modifiers ConstructorDeclarator Block
                        | ConstructorDeclarator Block
    '''
    revoutput.append(p.slice)
def p_ConstructorDeclarator(p):
    '''ConstructorDeclarator : Identifier SEPLEFTBRACE ParameterList SEPRIGHTBRACE
                            | Identifier SEPLEFTBRACE SEPRIGHTBRACE
    '''
    revoutput.append(p.slice)

def p_StaticInitializer(p):
    '''StaticInitializer : KEYSTATIC Block
    '''
    revoutput.append(p.slice)

def p_NonStaticInitializer(p):
    '''NonStaticInitializer : Block
    '''
    revoutput.append(p.slice)



##############################################################################################3
def p_Modifiers(p):
    '''Modifiers : Modifier
                | Modifiers Modifier
    '''
    revoutput.append(p.slice)
def p_Modifier(p):
    '''Modifier : KEYPUBLIC
                | KEYPROTECTED
                | KEYPRIVATE
                | KEYSTATIC
                | KEYFINAL
    '''
    revoutput.append(p.slice)
def p_Block(p):
    '''Block : SEPLEFTPARAN LocalVariableDeclarationsAndStatements SEPRIGHTPARAN
            | SEPLEFTPARAN SEPRIGHTPARAN 
    '''
    revoutput.append(p.slice)
def p_LocalVariableDeclarationsAndStatements(p):
    '''LocalVariableDeclarationsAndStatements : LocalVariableDeclarationOrStatement
                        | LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement
    '''
    revoutput.append(p.slice)
def p_LocalVariableDeclarationOrStatement(p):
    '''LocalVariableDeclarationOrStatement : LocalVariableDeclarationStatement
                                | Statement
    '''
    revoutput.append(p.slice)
def p_LocalVariableDeclarationStatement(p):
    '''LocalVariableDeclarationStatement : TypeSpecifier VariableDeclarators  SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_Statement(p):
    '''Statement : EmptyStatement
                | ExpressionStatement SEPSEMICOLON
                | LabelStatement
                | SelectionStatement
                | IterationStatement
                | JumpStatement
                | GuardingStatement
                | Block
    '''
    revoutput.append(p.slice)
def p_EmptyStatement(p):
    ''' EmptyStatement : SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_LabelStatement(p):
    ''' LabelStatement : Identifier SEPCOLON
                | KEYCASE ConstantExpression SEPCOLON
                | KEYDEFAULT SEPCOLON
    '''
    revoutput.append(p.slice)
def p_ExpressionStatement(p):
    '''ExpressionStatement : Expression
    '''
    revoutput.append(p.slice)

precedence = (
    ('right', 'THAN', 'KEYELSE'),
)

def p_SelectionStatement(p):
    '''SelectionStatement : KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement %prec THAN
                        | KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE Statement KEYELSE Statement
    '''
    revoutput.append(p.slice)
def p_IterationStatement(p):
    '''IterationStatement : KEYWHILE SEPLEFTBRACE Expression SEPRIGHTBRACE Statement
                        | KEYFOR SEPLEFTBRACE ForInt ForExpr ForIncr SEPRIGHTBRACE Statement
                        | KEYFOR SEPLEFTBRACE ForInt ForExpr SEPRIGHTBRACE Statement
    '''
    revoutput.append(p.slice)
def p_ForInt(p):
    '''ForInt : ExpressionStatements SEPSEMICOLON
            | LocalVariableDeclarationStatement
            | SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_ForExpr(p):
    '''ForExpr : Expression SEPSEMICOLON
            | SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_ForIncr(p):
    '''ForIncr : ExpressionStatements
    '''
    revoutput.append(p.slice)
def p_ExpressionStatements(p):
    '''ExpressionStatements : ExpressionStatement
                    | ExpressionStatements SEPCOMMA ExpressionStatement
    '''
    revoutput.append(p.slice)
def p_JumpStatement(p):
    '''JumpStatement : KEYBREAK Identifier SEPSEMICOLON
                | KEYBREAK SEPSEMICOLON
                | KEYCONTINUE Identifier SEPSEMICOLON
                | KEYCONTINUE SEPSEMICOLON
                | KEYRETURN Expression SEPSEMICOLON
                | KEYRETURN  SEPSEMICOLON
                | KEYTHROW Expression SEPSEMICOLON
    '''
    revoutput.append(p.slice)
def p_GuardingStatement(p):
    '''GuardingStatement : KEYTRY Block Finally
                        | KEYTRY Block Catches
                        | KEYTRY Block Catches Finally
    '''
    revoutput.append(p.slice)
def p_Catches(p):
    '''Catches : Catch
            | Catches Catch
    '''
    revoutput.append(p.slice)
def p_Catch(p):
    '''Catch : CatchHeader Block
    '''
    revoutput.append(p.slice)
def p_CatchHeader(p):
    '''CatchHeader : KEYCATCH SEPLEFTBRACE TypeSpecifier Identifier SEPRIGHTBRACE
                | KEYCATCH SEPLEFTBRACE TypeSpecifier SEPRIGHTBRACE
    '''
    revoutput.append(p.slice)
def p_Finally(p):
    '''Finally : KEYFINALLY Block
    '''
    revoutput.append(p.slice)
def p_PrimaryExpression(p):
    '''PrimaryExpression : QualifiedName
                    | NotJustName
    '''
    revoutput.append(p.slice)
def p_NotJustName(p):
    '''NotJustName : SpecialName
                | NewAllocationExpression
                | ComplexPrimary
    '''
    revoutput.append(p.slice)
def p_ComplexPrimary(p):
    '''ComplexPrimary : SEPLEFTBRACE Expression SEPRIGHTBRACE
            | ComplexPrimaryNoParenthesis
    '''
    revoutput.append(p.slice)
def p_ComplexPrimaryNoParenthesis(p):
    '''ComplexPrimaryNoParenthesis : BooleanLiteral
                            | IntegerLiteral
                            | FloatingLiteral
                            | CharacterLiteral
                            | StringLiteral
                            | ArrayAccess
                            | FieldAccess
                            | MethodCall
    '''
    revoutput.append(p.slice)
def p_ArrayAccess(p):
    '''ArrayAccess : QualifiedName SEPLEFTSQBR Expression SEPRIGHTSQBR
                | ComplexPrimary SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
    revoutput.append(p.slice)
def p_FieldAcess(p):
    '''FieldAccess : NotJustName SEPDOT Identifier
            | RealPostfixExpression SEPDOT Identifier
            | QualifiedName SEPDOT KEYTHIS
            | QualifiedName SEPDOT KEYCLASS
            | PrimitiveType SEPDOT KEYCLASS
    '''
    revoutput.append(p.slice)
def p_MethodCall(p):
    ''' MethodCall : MethodAccess SEPLEFTBRACE ArgumentList SEPRIGHTBRACE
            | MethodAccess SEPLEFTBRACE SEPRIGHTBRACE
    '''
    revoutput.append(p.slice)
def p_MethodAccess(p):
    ''' MethodAccess : ComplexPrimaryNoParenthesis
                | SpecialName
                | QualifiedName
    '''
    revoutput.append(p.slice)
def p_SpecialName(p):
    '''SpecialName : KEYTHIS
    '''
    revoutput.append(p.slice)
def p_ArgumentList(p):
    '''ArgumentList : Expression
            | ArgumentList SEPCOMMA Expression
    '''
    revoutput.append(p.slice)
def p_NewAllocationExpression(p):
    '''NewAllocationExpression : PlainNewAllocationExpression
                    | QualifiedName SEPDOT PlainNewAllocationExpression
    '''
    revoutput.append(p.slice)
def p_PlainNewAllocationExpression(p):
    '''PlainNewAllocationExpression :  ArrayAllocationExpression
                        | ClassAllocationExpression
                        | ArrayAllocationExpression SEPLEFTPARAN SEPRIGHTPARAN
                        | ClassAllocationExpression SEPLEFTPARAN SEPRIGHTPARAN
                        | ArrayAllocationExpression SEPLEFTPARAN ArrayInitializers SEPRIGHTPARAN
                        | ClassAllocationExpression SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
    '''
    revoutput.append(p.slice)
def p_ClassAllocationExpression(p):
    '''ClassAllocationExpression : KEYNEW TypeName SEPLEFTBRACE ArgumentList SEPRIGHTBRACE
                        | KEYNEW TypeName SEPLEFTBRACE SEPRIGHTBRACE
    '''
    revoutput.append(p.slice)
def p_ArrayAllocationExpression(p):
    '''ArrayAllocationExpression : KEYNEW TypeName DimExprs Dims
                            | KEYNEW TypeName DimExprs
                            | KEYNEW TypeName Dims
    '''
    revoutput.append(p.slice)
def p_DimExprs(p):
    '''DimExprs : DimExpr
                | DimExprs DimExpr
    '''
    revoutput.append(p.slice)
def p_DimExpr(p):
    '''DimExpr : SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
    revoutput.append(p.slice)
def p_Dims(p):
    '''Dims : OP_DIM
            | Dims OP_DIM
    '''
    revoutput.append(p.slice)
def p_PostfixExpression(p):
    '''PostfixExpression : PrimaryExpression
                    | RealPostfixExpression
    '''
    revoutput.append(p.slice)
def p_RealPostfixExpression(p):
    '''RealPostfixExpression : PostfixExpression OPINCREMENT
                    | PostfixExpression OPDECREMENT
    '''
    revoutput.append(p.slice)
def p_UnaryExpression(p):
    '''UnaryExpression : OPINCREMENT UnaryExpression
                | OPDECREMENT UnaryExpression
                | ArithmeticUnaryOperator CastExpression
                | LogicalUnaryExpression
    '''
    revoutput.append(p.slice)
def p_LogicalUnaryExpression(p):
    '''LogicalUnaryExpression : PostfixExpression
                        | LogicalUnaryOperator UnaryExpression
    '''
    revoutput.append(p.slice)
def p_LogicalUnaryOperator(p):
    '''LogicalUnaryOperator : OPTILDE
                         | OPNOT 
    '''
    revoutput.append(p.slice)
def p_ArithmeticUnaryOperator(p):
    '''ArithmeticUnaryOperator : OPPLUS
                            | OPMINUS
    '''
    revoutput.append(p.slice)
def p_CastExpression(p) :
    ''' CastExpression : UnaryExpression
                | SEPLEFTBRACE PrimitiveTypeExpression SEPRIGHTBRACE CastExpression
                | SEPLEFTBRACE ClassTypeExpression SEPRIGHTBRACE CastExpression
                | SEPLEFTBRACE Expression SEPRIGHTBRACE LogicalUnaryExpression
    '''
    revoutput.append(p.slice)
def p_PrimitiveTypeExpression(p):
    '''PrimitiveTypeExpression : PrimitiveType
                    | PrimitiveType Dims
    '''
    revoutput.append(p.slice)
def p_ClassTypeExpression(p):
    '''ClassTypeExpression : QualifiedName Dims
    '''
    revoutput.append(p.slice)
def p_MultiplicativeExpression(p):
    '''MultiplicativeExpression : CastExpression
                    | MultiplicativeExpression OPMULTIPLY CastExpression
                    | MultiplicativeExpression OPDIVIDE CastExpression
                    | MultiplicativeExpression OPMOD CastExpression
    '''
    revoutput.append(p.slice)
def p_AdditiveExpression(p):
    '''AdditiveExpression : MultiplicativeExpression
                        | AdditiveExpression OPPLUS MultiplicativeExpression
                        | AdditiveExpression OPMINUS MultiplicativeExpression
    '''
    revoutput.append(p.slice)
def p_ShiftExpression(p):
    '''ShiftExpression : AdditiveExpression
                    | ShiftExpression OPLEFTSHIFT AdditiveExpression
                    | ShiftExpression OPRIGHTSHIFT AdditiveExpression
                    | ShiftExpression OPLOGICALSHIFT AdditiveExpression
    '''
    revoutput.append(p.slice)
def p_RelationalExpression(p):
    '''RelationalExpression : ShiftExpression
                        | RelationalExpression OPLESSER ShiftExpression
                        | RelationalExpression OPGREATER ShiftExpression
                        | RelationalExpression OPLESSEQ ShiftExpression
                        | RelationalExpression OPGREATEQ ShiftExpression
                        | RelationalExpression OPINSTANCEOF TypeSpecifier
    '''
    revoutput.append(p.slice)
def p_EqualityExpression(p):
    '''EqualityExpression : RelationalExpression
                        | EqualityExpression OPCHECKEQ RelationalExpression
                        | EqualityExpression OPNOTEQ RelationalExpression
    '''
    revoutput.append(p.slice)
def p_AndExpression(p):
    '''AndExpression : EqualityExpression
                    | AndExpression OPBINAND EqualityExpression
    '''
    revoutput.append(p.slice)
def p_ExclusiveOrExpression(p):
    '''ExclusiveOrExpression : AndExpression
                    | ExclusiveOrExpression OPXOR AndExpression
    '''
    revoutput.append(p.slice)
def p_InclusiveOrExpression(p):
    '''InclusiveOrExpression : ExclusiveOrExpression
                        | InclusiveOrExpression OPBINOR ExclusiveOrExpression
    '''
    revoutput.append(p.slice)
def p_ConditionalAndExpression(p):
    '''ConditionalAndExpression : InclusiveOrExpression
                            | ConditionalAndExpression OPAND InclusiveOrExpression
    '''
    revoutput.append(p.slice)
def p_ConditionalOrExpression(p):
    '''ConditionalOrExpression : ConditionalAndExpression
                        | ConditionalOrExpression OPOR ConditionalAndExpression
    '''
    revoutput.append(p.slice)
def p_ConditionalExpression(p):
    ''' ConditionalExpression : ConditionalOrExpression
                        | ConditionalOrExpression OPTERNARY Expression SEPCOLON ConditionalExpression
    '''
    revoutput.append(p.slice)
def p_AssignmentExpression(p):
    '''AssignmentExpression : ConditionalExpression
                        | UnaryExpression AssignmentOperator AssignmentExpression
    '''
    revoutput.append(p.slice)
def p_AssignmentOperator(p):
    ''' AssignmentOperator : OPEQUAL
                        | OPMULTIPLYEQ
                        | OPDIVIDEEQ
                        | OPMODEQ
                        | OPPLUSEQ
                        | OPMINUSEQ
                        | OPLEFTSHIFTEQ
                        | OPRIGHTSHIFTEQ
                        | OPLOGICALSHIFTEQ
                        | OPBINANDEQ
                        | OPXOREQ
                        | OPBINOREQ
    '''
    revoutput.append(p.slice)
def p_Expression(p):
    '''Expression : AssignmentExpression
    '''
    revoutput.append(p.slice)
def p_ConstantExpression(p):
    '''ConstantExpression : ConditionalExpression
    '''
    revoutput.append(p.slice)
def p_error(p):
    if p == None:
        print str(sys.argv[1])+" ::You missed something at the end"
    else:
        print str(sys.argv[1])+" :: Syntax error in line no " +  str(p.lineno)

def rightderivation(prefx,sufx):
    global finalout
    global countg
    lcount=countg
    count=0
    last=[]
    for i in range(1,len(output[lcount])):
        if not (output[lcount][i] in nonterminals):
            count+=1
        else:
            last.append(i)
    pre=" "
    for i in range(1,len(output[lcount])):
        if(last != [] and i==last[-1]):
            pre=pre+" <b> "+str(valuate(lcount,i))  +" </b> "
        else:
            pre=pre+str(valuate(lcount,i)) +  " "
    if(count==len(output[lcount])-1):
        countg+=1
        return pre
    del last[-1]
    finalout.append(computestr(prefx)+" " + pre+" " +sufx)
    suf=" "
    for x in range(len(output[lcount])-1,0,-1):
        if not (output[lcount][x] in nonterminals):
            suf = valuate(lcount,x)+suf
            continue
        las =-1
        if(numnonterminals(countg+1)==0 and last==[]):
            for i in range(len(prefx)-1,-1,-1):
                if prefx[i] in nonterminals:
                    las=i
                    break
            pre=" "
            for i in range(len(prefx)):
                if(i==las):
                    pre=pre+" <b> "+str(prefx[i])  +" </b> "
                elif prefx[i] in nonterminals:
                    pre=pre+str(prefx[i]) +  " "
                else:
                    pre=pre+str(prefx[i].value)+  " "
            flag=0
        else:
            pre=computestr(prefx)
            flag=1
        for i in range(1,x):
            if(flag ==1 and last != [] and i==last[-1] ): 
                pre=pre+" <b> "+str(valuate(lcount,i))  +" </b> "
            else:
                pre=pre+str(valuate(lcount,i))+" "
        countg+=1
        suf = str(rightderivation(prefx+output[lcount][1:x],suf+sufx)) +" " + suf
        countg-=1
        finalout.append(pre+" " +suf+" " +sufx)
        if (last != []):
            del last[-1]
    countg+=1
    return suf

def computestr(lis):
    stri=" "
    for i in range(len(lis)):
        if lis[i] in nonterminals:
            stri=stri+str(lis[i]) +  " "
        else:
            stri=stri+str(lis[i].value)+  " "
    return stri

def valuate(line,x):
    if output[line][x] in nonterminals:
        return output[line][x]
    else:
        return output[line][x].value

def numnonterminals(line):
    # print output[line]
    count=0
    for i in range(1,len(output[line])):
        if output[line][i] in nonterminals:
            count+=1
    # print count
    return count

def truncfinal():
    global finalout
    i=0
    while i < len(finalout)-1:
        if(removeempty(finalout[i].split(' '))==removeempty(finalout[i+1].split(' '))):
            del finalout[i+1]
        else:
            # print "truncfinal"
            # print finalout[i]
            # print finalout[i+1]
            i+=1


def removeempty(lis):
    i=0
    while i < len(lis):
        if(lis[i]=='' or lis[i]=='<b>' or lis[i]=='</b>'):
            del lis[i]
        else:
            i+=1
    return lis

yacc.yacc()

a=open(sys.argv[1],'r')
a=a.read()
data = ""
a+="\n"
yacc.parse(a)
filename=sys.argv[1]
fnstart=0
fnend=0
for j in range(len(filename)):
    if filename[j]=='/':
        fnstart=j
    if filename[j]=='.':
        fnend=j
filename=filename[fnstart+1:fnend]
import sys
sys.stdout = open(str(filename)+".html", 'w')

# a=a.split('\n')
# for s in a:
#     if not (s == ''): 
#         # data += " " +s
#         yacc.parse(s)

for i in range(len(revoutput)):
    nonterminals.append(revoutput[i][0])
for i in range(len(revoutput)-1,-1,-1):
    output.append(revoutput[i])
# for i in output:
#     print i
print "<html> <head> <title> Rightmost derivation </title> </head> <body bgcolor='#E6E6FA'>"
print "<h2> Rightmost Derivation of the code</h2>"
print  "<b style = color:red> "+ str(output[0][0])+"</b> "+ "</br>"
rightderivation([],"")
truncfinal()
for i in finalout:
    sp=i.split(' ')
    st=""
    for j in range(len(sp)):
        if sp[j]=='':
            continue
        if sp[j]=='<b>':
            st+="<b style = color:red> "
        else:
            st+=sp[j]+ " "
    print st + "</br>"
print "</body></html>"
