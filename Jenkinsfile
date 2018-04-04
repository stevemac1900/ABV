node
{
    stage('Fetch')
    {
        checkout scm
    }
    stage('Unit Testing')
    {
        sh 'tox'
    }
    stage('Static Analysis')
    {
        sh 'pylint src/abv/*.py tests/*.py'
    }
}