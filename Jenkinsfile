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
        sh 'pylint'
    }
    stage('Coverage')
    {
        sh 'pytest --cov=abv --cov-fail-under=90'
    }
}