<?php
$auth_url  = "http://search.isiknowledge.com/esti/wokmws/ws/WOKMWSAuthenticate?wsdl";
$auth_client = @new SoapClient($auth_url);
$auth_response = $auth_client->authenticate();
$search_url = "http://search.isiknowledge.com/esti/wokmws/ws/WokSearchLite?wsdl";
$search_client = @new SoapClient($search_url);
$search_client->__setCookie('SID',$auth_response->return);
$search_array = array(
  'queryParameters' => array(
    'databaseID' => 'WOS',
    'userQuery' => 'AU=Douglas T*',
    'editions' => array(
      array('collection' => 'WOS', 'edition' => 'SSCI'),
      array('collection' => 'WOS', 'edition' => 'SCI')
    ),
    'queryLanguage' => 'en'
  ),
  'retrieveParameters' => array(
    'count' => '5',
    'fields' => array(
      array('name' => 'Date', 'sort' => 'D')
    ),
    'firstRecord' => '1'
  )
);
try{
  $search_response = $search_client->search($search_array);
} catch (Exception $e) {  
    echo $e->getMessage(); 
}
print_r($search_response);
?>
