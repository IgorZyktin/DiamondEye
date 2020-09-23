% rebase('base.tpl')
<div class="content">
    % for uuid, url_thumb in images:
    <div class="envelope">
        <a href="/browse/{{ uuid }}"><img src="{{ url_thumb }}" alt=""/></a>
    </div>
    % end
</div>
