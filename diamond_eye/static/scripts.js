function request(url, on_success, on_fail) {
    // common ajax call function
    let xhr = new XMLHttpRequest();
    xhr.open('POST', url, false);
    xhr.send();

    if (xhr.status !== 200) {
        alert(xhr.status + ': ' + xhr.statusText);
        if (on_fail !== null) on_fail();
    } else {
        if (on_success !== null) on_success();
    }
    return false;
}

function saveState() {
    // dump current state to JSON file
    request('/save_state', setStateSaved, setStateNotSaved);
    return false;
}

function setStateSaved() {
    // remove red color from state button
    document.getElementById('save_btn').classList.remove('not_saved');
    return false;
}

function setStateNotSaved() {
    // add red color to the state button
    document.getElementById('save_btn').classList.add('not_saved');
    return false;
}

function refreshState() {
    // rebuild state from the scratch
    request('/refresh_state', setStateSaved, function (){
        setStateNotSaved();
        window.location.reload();
    });
    return false;
}

function confirmAll() {
    // confirm loading of all of the images
    request('/save_all_unconfirmed', function () {
        setStateNotSaved();
        goSearch();
    }, null);
    return false;
}

function dropAll() {
    // cancel loading of all of the images
    if (confirm('Are you sure about that?')) {
        request('/drop_all_unconfirmed', function () {
            setStateNotSaved();
            goSearch();
        }, null);
    }
    return false;
}

function goSearch() {
    // start searching with specified parameters
    let selector = document.getElementById('images_at_once')
    let query = `/search?at_once=${selector.value}`;
    window.location.href = query;
    return false;
}

function addTagBatch() {
    // add tag to whole set of uploaded images
    alert('addTagBatch');
    return false;
}

function addTag(div_id) {
    // add tag to a single image
    let node = document.getElementById(div_id);
    let div = document.createElement('div');
    let key = document.createElement('input')
    let value = document.createElement('input')
    let drop = document.createElement('a')

    div.className = 'f_row';
    key.type = 'text';
    value.type = 'text';
    key.placeholder = 'Tag name';
    value.placeholder = 'Tag value';
    key.classList.add('tag_key');
    value.classList.add('tag_value');
    drop.classList.add('tag_drop', 'btn');
    drop.innerHTML = '-';
    drop.onclick = function () {
        dropTag(div_id, drop);
    };

    div.append(key);
    div.append(value);
    div.append(drop);

    node.append(div);
    return false;
}

function dropTagBatch() {
    // drop tag from all images
    alert('dropTagBatch');
    return false;
}

function dropTag(div_id, button) {
    // delete tag from a single image
    let node = document.getElementById(div_id);
    for (let i = 0; i < node.childElementCount; i++) {
        let del_button = node.children[i].children[2];
        if (Object.is(button, del_button)) {
            node.children[i].remove();
            break
        }
    }
    return false;
}

function confirmChanges(){
    // confirm changes in image tags
    alert('confirmChanges');
}
