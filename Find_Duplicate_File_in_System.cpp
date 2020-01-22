class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        vector<vector<string>> result;
        vector<string> dupFiles;
        string directory, file, content, path, key;
        unordered_multimap<string, string> dupCheck; // key:content, value: directory
        set<string> keys;
        size_t pos;
        //auto range = dupCheck.equal_range("a");
        pair<unordered_multimap<string, string>::iterator,unordered_multimap<string, string>::iterator> range;
        
        for(auto iter = paths.begin(); iter != paths.end();iter++){
            directory = "";
            content = "";
            file = "";
            path = *iter;
            
            //split directory
            pos = path.find(' ');
            directory = path.substr(0,pos);
            path = path.substr(pos+1);
            
            //split filename and content
            while(path.length() >0){
                //delete space
                if(path[0] == ' '){
                    path = path.substr(1);
                }
                pos = path.find('(');
                file = path.substr(0,pos);
                path = path.substr(pos+1);
                pos = path.find(')');
                content = path.substr(0,pos);
                path = path.substr(pos+1);
                dupCheck.insert(make_pair(content, directory+'/'+file));
                keys.insert(content);
            }
        }
        
        //add duplicated files to result
        for(auto it_key = keys.begin();it_key != keys.end(); it_key++){
            key = *it_key;
            if(dupCheck.count(key) >1 ){
                dupFiles.clear();
                range = dupCheck.equal_range(key);
                for(auto iter = range.first; iter!= range.second;iter++){
                    dupFiles.push_back(iter->second);
                }
                //sort(dupFiles.begin(),dupFiles.end());
                result.push_back(dupFiles);
            }
        }
        
        return result;
    }
};
